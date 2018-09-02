import pandas as pd
import numpy as np
from gensim import corpora

def trim_dictionary(dictionary):
    dictionary.filter_extremes(no_below=3, no_above=0.5, keep_n=100000, keep_tokens=None)

if __name__ == '__main__':
    dictionary = corpora.Dictionary.load('../data/emails_all_terms.dict')
    trim_dictionary(dictionary)
    dictionary.save('../data/emails_trimmed_terms.dict')
