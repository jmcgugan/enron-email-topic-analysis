'''
Create saved corpus files from saved period files and saved dictionary or
dictionaries.
'''

import os
import pandas as pd
from gensim import corpora

def make_corpora(dictionary, periods_dir, out_dir):
    '''
    Iterate through periods_dir, loading all the email dataframes for each
    time period, making a corpus for each, and writing it to out_dir
    '''
    periods_dir = periods_dir + '/'
    out_dir = out_dir + '/'
    for fname in os.listdir(periods_dir):
      emails = load(periods_dir + fname)
      doc2terms = emails.terms.tolist()
      corpus = [ dictionary.doc2bow(terms) for terms in doc2terms ]
      corpora.MmCorpus.serialize(out_dir + fname.split('.')[0] + '.mm', corpus)

def load(infilename):
    '''
    Read wide dataframe from infilename & return a dataframe sorted by Date.
    '''
    emails = pd.read_pickle(infilename)
    emails['Date'] = pd.to_datetime(emails['Date'], infer_datetime_format=True)
    emails = emails.sort_values('Date')
    #emails = emails.set_index('Date')
    return emails

def make():
    dictionary = corpora.Dictionary.load('../data/emails_all_terms.dict')
    make_corpora(dictionary, '../data/periods', '../data/corpora_from_all')
    dictionary = corpora.Dictionary.load('../data/emails_trimmed_terms.dict')
    make_corpora(dictionary, '../data/periods', '../data/corpora_from_trimmed')

if __name__ == '__main__':
    make()
