import os
from gensim import corpora, models, similarities
import pyLDAvis
import pyLDAvis.gensim

def make_lda_visualizations(corpora_dir, model_dir, vis_dir):
    '''Iterate through the lda models in model_dir and the corpora stored in
    corpora_dir, creating pyLDAvis visualizations for all the models stored
    therein. Write the resulting visualizations out to files in vis_dir.
    '''
    corpora_dir = corpora_dir + '/'
    model_dir = model_dir + '/'
    vis_dir = vis_dir + '/'
    for fname in sorted({fn.split('.')[0] for fn in os.listdir(model_dir)}):
        make_lda_visualization(corpora_dir, model_dir, vis_dir, fname)

def make_lda_visualization(corpora_dir, model_dir, vis_dir, fname):
    '''Make a single pyLDAvis visualization by loading the corpus and dictionary
    stored in corpora_dir fname, coupling it with the corresponding model stored
    in model_dir and writing the visualization out to a file in vis_dir. All
    files are linked by sharing the same file name.
    '''
    dictionary = corpora.Dictionary.load(corpora_dir + fname + '.dict')
    corpus = corpora.MmCorpus(corpora_dir + fname + '.mm')
    model = models.LdaModel.load(model_dir + fname + '.lda')
    davis = pyLDAvis.gensim.prepare(model, corpus, dictionary)
    pyLDAvis.save_html(davis, vis_dir + fname + '.html')

if __name__ == '__main__':
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-06-01 00:00:00 thru 2001-06-30 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-07-01 00:00:00 thru 2001-07-31 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-08-01 00:00:00 thru 2001-08-31 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-09-01 00:00:00 thru 2001-09-30 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-10-01 00:00:00 thru 2001-10-31 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-11-01 00:00:00 thru 2001-11-30 23:59:59')
    make_lda_visualization('../data/corpora/', '../data/lda/','../data/ldavis/', '2001-12-01 00:00:00 thru 2001-12-31 23:59:59')
    # make_lda_visualizations('../data/corpora', '../data/lda', '../data/ldavis')
