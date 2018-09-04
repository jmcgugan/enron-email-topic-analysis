import os
from collections import Counter
from gensim import corpora, models
import pickle

def count():
    counters = {}
    dictionary = corpora.Dictionary.load('../data/emails_all_terms.dict')
    corpora_dir = '../data/corpora_from_all/'
    model_dir = '../data/lda_from_all/'
    for fname in sorted({fn.split('.')[0] for fn in os.listdir(model_dir)}):
        cntr = Counter()
        corpus = corpora.MmCorpus(corpora_dir + fname + '.mm')
        model = models.LdaMulticore.load(model_dir + fname + '.lda')
        top = model.top_topics(corpus=corpus, dictionary=dictionary)
        for topic in top:
            word_list = topic[0]
            for prob, word in word_list:
                cntr[word] += 1
        counters[fname] = counters
    return counters

if __name__ == '__main__':
    counters = count()

    for date, counter in sorted(counters.items()):
        if 'california' in counter:
            print(date + '\t' + str(counter['california']) + '\n')
        else:
            print(date + '\t' + str(0) + '\n')

    with open('../data/term_counts.pkl', 'wb') as handle:
        pickle.dump(counters, handle, protocol=pickle.HIGHEST_PROTOCOL)
