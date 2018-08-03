import os
from gensim import corpora, models, similarities

def make_lda_models(corpora_dir, model_dir, num_topics=400):
    '''Iterate through corpora_dir, loading all the dictionaries and corpora
    stored there and writing LDA models into model_dir.
    '''
    corpora_dir = corpora_dir + '/'
    for fname in sorted({fn.split('.')[0] for fn in os.listdir(corpora_dir)}):
        make_lda_model(corpora_dir, model_dir, fname, num_topics=num_topics)

def make_lda_model(corpora_dir, model_dir, fname, num_topics=400):
    '''Make a single LDA model by loading the corpus and dictionary stored in
    corpora_dir fname, buiding the model, and writing it out to model_dir
    '''
    dictionary = corpora.Dictionary.load(corpora_dir + fname + '.dict')
    corpus = corpora.MmCorpus(corpora_dir + fname + '.mm')
    lda_model = models.LdaModel(corpus, id2word=dictionary, num_topics=num_topics)
    lda_model.save(model_dir + '/' + fname + '.lda')

if __name__ == '__main__':
    # make_lda_model('../data/corpora/', '../data/lda','2001-01-01 00:00:00 thru 2001-01-31 23:59:59')
    make_lda_models('../data/corpora', '../data/lda')
