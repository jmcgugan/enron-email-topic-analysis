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

def tokenize(doc):
    '''
    Take a string, presumably representing a single document. Tokenize it,
    strip stop words and puctuation, stem it, lemmatize it. Return a list of
    tokens.
    '''
    stops = set(stopwords.words('english'))
    stops.update(("to","cc","subject","http","from","sent","www","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
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

def make_dictionary(docs, rare=0):
    '''
    Make gensim dictionaries for a list of documents.
    Inputs: list of documents
            rare_common is a list of tuples. The first element of each
                tuple is the rare_limit, the second is the common_limit.
                Only terms occurring more frequently than rare_limit will be
                included.
                Only terms whose
    Output: (doc2terms, gensim dictionary)
    '''
    doc2terms = []
    for doc in docs:
        doc2terms.append(tokenize(doc))

    # Eliminate all terms used too rarely or too commonly in the corpus since
    # they are useless for clustering (though rare terms are useful for search)
    if rare>0:
        frequency = defaultdict(int)
        for doc in doc2terms:
            for term in doc:
                frequency[term] += 1
        doc2terms =   [   [term for term in doc \
                                if (frequency[term] > rare) \
                        ]\
                        for doc in doc2terms
                        ]
    term2id_dict = corpora.Dictionary(doc2terms)

    return term2id_dict

if __name__ == '__main__':
    emails = pd.read_csv('../data/emails_wide.csv')
    dictionary = make_dictionary(emails.content)
    dictionary.save('../data/emails.dict')
