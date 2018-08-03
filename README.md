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

We propose to analyze the Enron dataset less from the fraud perspective and more from the prospective that these are real emails exchanged within a single corporation as part of the daily life of that corporation.

## Data analysis

The corpus consists of over 500,000 emails, mainly covering a two year period 2000-2001.

1. The source data is in standard email format, i.e. a multipart format with To, From, Subject… metadata plus a possibly multipart MIME payload. This was parsed to a "wide" dataframe with separate columns for To, From, content, etc.
