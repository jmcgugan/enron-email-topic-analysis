import pandas as pd
from gensim import corpora, models
# import matplotlib.pyplot as plt

def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    for num_topics in range(start, limit, step):
        #model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word)
        model = models.LdaMulticore(corpus, id2word=dictionary, num_topics=num_topics)
        model.save('../data/topic_optimization/' + str(num_topics) + ' topics.lda')
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    return coherence_values

def find_optimal_num_topics():
    emails = pd.read_pickle('../data/periods/2001-01.pkl')
    tokenized_texts = emails['terms'].tolist()
    dictionary = corpora.Dictionary.load('../data/emails_trimmed_terms.dict')
    corpus = corpora.MmCorpus('../data/corpora_from_trimmed/2001-01.mm')
    coherence_values = \
        compute_coherence_values(dictionary, corpus, tokenized_texts, start=50, limit=501, step=50)
    with open('../data/topic_coherence_for_trimmed_dict_2001-01.pkl', 'wb') as handle:
        pickle.dump(coherence_values, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Print the coherence scores
    limit=501; start=50; step=50;
    x = range(start, limit, step)
    for m, cv in zip(x, coherence_values):
        print("Num Topics = " + str(m) + "\thas Coherence Value of " + str(round(cv, 4)))
    # Generate plot
    #plt.plot(x, coherence_values)
    #plt.xlabel("Num Topics")
    #plt.ylabel("Coherence score")
    #plt.legend(("coherence_values"), loc='best')
    #plt.savefig('../data/topic_coherence_for_trimmed_dict_2001-01.png')

if __name__ == '__main__':
    find_optimal_num_topics()
