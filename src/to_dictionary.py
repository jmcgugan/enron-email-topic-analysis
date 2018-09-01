import numpy as np
import pandas as pd

from gensim import corpora

def make_dictionary(doc2terms):
    '''
    Make a gensim dictionary for a list of documents.
    Inputs: list of lists. Outer list represents docs, inner is list of tokens
    or terms for each doc.
    Output: gensim dictionary
    '''
    term2id_dict = corpora.Dictionary(doc2terms)

    return term2id_dict

if __name__ == '__main__':
    emails = pd.read_pickle('../data/emails_wide_terms.pkl')
    dictionary = make_dictionary(emails.terms.tolist())
    dictionary.save('../data/emails_all_terms.dict')
