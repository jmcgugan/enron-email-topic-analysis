# Topic Analysis of the Enron Email Corpus  
## _The Problem of a Big, Rapidly Changing Corpus_

**Jim McGugan**

![Enron Image](images/enron-mugs.jpeg)

## Problem

*Email!* Can't live with it; can't live without it. It's the bane of corporate life. Most large organizations run on email. [One study](https://www.huffingtonpost.com/entry/check-work-email-hours-survey_us_55ddd168e4b0a40aa3ace672) found American workers spend 6.3 hours per day on email. [Another study](https://mashable.com/2012/08/01/email-workers-time/#gTF9bAOY2EqD) pegs it at only 28% of workers' time.

Email has certainly been much studied by the Data Science community, but most studies have focused on [spam detection](https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering). A problem with non-spam analysis of email is that most corporations and government departments do not want to make their email troves available for analysis as they contain sensitive information.

A pleasant exception to the non-availability of good email samples is the [Enron dataset](http://www.cs.cmu.edu/~./enron/) which has entered the public domain as a result of Enron's collapse and the resulting criminal investigation of the company. The dataset includes over half a million emails exchanged by 150 employees of Enron. The [Wikipedia article](https://en.wikipedia.org/wiki/Enron_Corpus) on it comments *"The corpus is unique in that it is one of the only publicly available mass collections of real emails easily available for study, as such collections are typically bound by numerous privacy and legal restrictions which render them prohibitively difficult to access."*

The Enron dataset is well-known in the Data Science community but much of the study of it has emphasized [fraud detection](https://linkurio.us/blog/investigating-the-enron-email-dataset/). It has recently been imported as a [Kaggle dataset](https://www.kaggle.com/wcukierski/enron-email-dataset) but relatively little analysis beyond basic exploration has yet been performed on it.

### Generalization of the Study

More generally, this study looks at what the data scientist can do with a big, rapidly changing dataset. This occurs not just in email, but in all social media (Facebook, Twitter, etc.) as well as news feeds. Presumably the topics change over time.

### Main questions

1. Are there discernable topics?

2. Do these topics change over time?

## Data analysis

The corpus consists of over 500,000 emails, mainly covering a two year period 2000-2001.

1. The

We propose to analyze the Enron dataset less from the fraud perspective and more from the prospective that these are real emails exchanged within a single corporation as part of the daily life of that corporation.

###Topic Analysis

What do these emails talk about? We propose to perform a variety of topic analyses, including TF-IDF, SVD, and NMF to see if we can identify latent topic clusters in the data. It will be particularly interesting to associate topics with people.

As a stretch objective, we would like to progress beyond the "bag of words" approach. I am particularly drawn to the [Positive Pointwise Mutual Information (PPMI) technique](https://en.wikipedia.org/wiki/Pointwise_mutual_information#mw-head) which looks at words in context. It is a natural progression from Naive Bayes as it works by looking at the ratio of the joint probability of word i and word j to the Naive Bayes assumption of P(Wi)*P(Wj).

It would seem that PPMI is somewhat underused in Python because there is [no prebuilt implementation of it](https://stackoverflow.com/questions/22118350/python-sentiment-analysis-using-pointwise-mutual-information). As a *stretch* objective, I would like to try coding PPMI.

###How Efficient is Email?

We all have the experience of receiving vastly more email than we need. We could take the view that an email is either actioned or it is not. Actions consist of replying, forwarding, or at least filing the email in a subject folder. We could take the perspective that an email which is received and not actioned is of dubious usefulness to the recipient. What is the ratio of actioned emails to received emails?

##Network Analysis

What can we say about the links between individuals implied by email traffic? Are there connectors who stand between different communities?

##Analysis of the Proposal

We appreciate that a good proposal consists of a good question plus good data. We think we have good data for this proposal but the questions are a bit diffuse at the moment. That is probably the biggest weakness of the proposal.

Nevertheless, the author has existed in the corporate world for many years and knows well the daily agony of getting to inbox 0. I am very keen on assessing the efficiency of email as a vehicle for coporate communication.
