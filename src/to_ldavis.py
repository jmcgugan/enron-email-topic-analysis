import os
from gensim import corpora, models, similarities
import pyLDAvis
import pyLDAvis.gensim

def make_lda_visualizations(dictionary, corpora_dir, model_dir, vis_dir):
    '''
    Iterate through the lda models in model_dir and the corpora stored in
    corpora_dir, creating pyLDAvis visualizations for all the models stored
    therein. Write the resulting visualizations out to files in vis_dir.
    '''
    corpora_dir = corpora_dir + '/'
    model_dir = model_dir + '/'
    vis_dir = vis_dir + '/'
    for fname in sorted({fn.split('.')[0] for fn in os.listdir(model_dir)}):
        make_lda_visualization(dictionary,corpora_dir, model_dir, vis_dir, fname)

def make_lda_visualization(dictionary, corpora_dir, model_dir, vis_dir, fname):
    '''
    Make a single pyLDAvis visualization by loading the corpus and dictionary
    stored in corpora_dir fname, coupling it with the corresponding model stored
    in model_dir and writing the visualization out to a file in vis_dir. All
    files are linked by sharing the same file name.
    '''
    corpus = corpora.MmCorpus(corpora_dir + fname + '.mm')
    model = models.LdaModel.load(model_dir + fname + '.lda')
    davis = pyLDAvis.gensim.prepare(model, corpus, dictionary)
    pyLDAvis.save_html(davis, vis_dir + fname + '.html')

def make():
    dictionary = corpora.Dictionary.load('../data/emails_all_terms.dict')
    make_lda_visualizations(\
        dictionary,\
        '../data/corpora_from_all', \
        '../data/lda_from_all', \
        '../data/ldavis_from_all')
    dictionary = corpora.Dictionary.load('../data/emails_trimmed_terms.dict')
    make_lda_visualizations(\
        dictionary,\
        '../data/corpora_from_trimmed', \
        '../data/lda_from_trimmed', \
        '../data/ldavis_from_trimmed')

if __name__ == '__main__':
    make()
