import numpy as np
import pandas as pd
import string
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import defaultdict

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

def add_terms_col(df):
    '''
    Add a terms column to the emails df.
    '''
    df['terms'] = df['content'].map(tokenize)
    return df

if __name__ == '__main__':
    emails = pd.read_csv('../data/emails_wide.csv')
    add_terms_col(emails)
    emails.to_pickle('../data/emails_wide_terms.pkl')
