import numpy as np
import pandas as pd
import datetime
import string
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import defaultdict
from gensim import corpora


def load(infilename):
    '''Read wide CSV file from infilename & return a dataframe sorted by Date.
    '''
    emails = pd.read_csv(infilename)
    emails['Date'] = pd.to_datetime(emails['Date'], infer_datetime_format=True)
    emails = emails.sort_values('Date')
    #emails = emails.set_index('Date')
    return emails

def get_periods():
    '''Return a sorted list of datetime pairs representing consecutive periods.
    Note: this code currently only returns one month periods between Jan 1 2000
    and Dec 31 2001, roughly matching the Enron corpus' duration. The idea is
    to eventually generalize it to other period types like week and quarter.
    '''
    periods = []
    for year in range(2000,2002):
        for month in range(1,13):
            start = datetime.datetime(year,month,1,0,0,0)
            if month in {1,3,5,7,8,10,12}:
                last_day = 31
            elif (month == 2):
                if (year % 4) == 0:
                    last_day = 29
                else:
                    last_day = 28
            else:
                last_day = 30
            end = datetime.datetime(year,month,last_day,23,59,59)
            periods.append( (start, end) )
    return periods

def tokenize(doc):
    ''' Take a string, presumably representing a single document. Tokenize it,
    strip stop words and puctuation, stem it, lemmatize it. Return a list of
    tokens.
    '''
    stops = set(stopwords.words('english'))
    stops.update(("to","cc","subject","http","from","sent","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    exclude = set(string.punctuation)
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    doc = doc.rstrip()
    doc = re.sub(r'[^a-zA-Z]', ' ', doc)
    punc_free = ''.join(ch for ch in doc if ch not in exclude)
    stop_free = [word for word in punc_free.lower().split() if((word not in stops) and (not word.isdigit()))]
    stem_free = [stemmer.stem(word) for word in stop_free]
    lemmed = [lemmatizer.lemmatize(word) for word in stem_free]
    return lemmed

def make_corpora(infilename, outdir, dates=None):
    emails_df = load(infilename)
    if dates == None:
        periods = get_periods()
    else:
        periods = [ dates ]
    for start, end in periods:
        emails_for_period = \
            emails_df[ (emails_df['Date'] >= start) & (emails_df['Date'] <= end)]['content']
        corpus, dictionary = make_corpus(emails_for_period)
        filestub = outdir + '/' + str(start) + ' thru ' + str(end)
        corpora.MmCorpus.serialize(filestub + '.mm', corpus)
        dictionary.save(filestub + '.dict')

def make_corpus(docs, strip_singletons=True):
    '''Make a gensim corpus for a list of documents.
    Inputs: list of documents
            strip_singletons boolean to indicate whether to strip all terms
                that occur only once in the corpus. Default is True.
    Output: (gensim corpus, gensim dictionary)
    '''
    doc2terms_array = []
    for doc in docs:
        doc2terms_array.append(tokenize(doc))

    # Elminate all terms used once only in the corpus since they are useless
    # for clustering (though would be very useful for searching)
    if strip_singletons:
        frequency = defaultdict(int)
        for doc in doc2terms_array:
            for term in doc:
                frequency[term] += 1
        doc2terms = [ [term for term in doc if frequency[term] > 1]
                    for doc in doc2terms_array]

    term2id_dict = corpora.Dictionary(doc2terms_array)
    doc2ids_array = [term2id_dict.doc2bow(terms) for terms in doc2terms_array]

    return (doc2ids_array, term2id_dict)

if __name__ == '__main__':
  make_corpora('../data/emails_wide.csv', '../data/corpora')
