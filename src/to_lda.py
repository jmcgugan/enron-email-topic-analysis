import os
from gensim import corpora, models, similarities

def make():
    dictionary = corpora.Dictionary.load('../data/emails_all_terms.dict')
    make_lda_models(dictionary, '../data/corpora_from_all', '../data/lda_from_all')
    dictionary = corpora.Dictionary.load('..data/emails_trimmed_terms.dict')
    make_lda_models(dictionary, '..data/corpora_from_trimmed', '../data/lda_from_trimmed')

def make_lda_models(dictionary, corpora_dir, model_dir, num_topics=400):
    '''Iterate through corpora_dir, loading all the dictionaries and corpora
    stored there and writing LDA models into model_dir.
    '''
    corpora_dir = corpora_dir + '/'
    for fname in sorted({fn.split('.')[0] for fn in os.listdir(corpora_dir)}):
        corpus = corpora.MmCorpus(corpora_dir + fname + '.mm')
        lda_model = models.LdaMulticore(corpus, id2word=dictionary, num_topics=num_topics)
        lda_model.save(model_dir + '/' + fname + '.lda')

if __name__ == '__main__':
    make()
