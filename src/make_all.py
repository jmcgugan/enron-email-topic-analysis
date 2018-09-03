'''
This module rebuilds the entire chain of files starting from the emails.csv
originally downloaded from kaggle. It ought to be called rarely as rebuilding
takes quite a bit of time. The whole reason for having each stage of the pipeline
write intermediate files is to avoid rebuilding from scratch every time. As such
this file exists as much for documentation of the correct order of steps.
'''

import parse_email_to_wide
import to_terms
import to_dictionary
import to_trimmed_dictionary
import to_periods
import to_corpora
import to_lda
import to_ldavis

if __name__ == '__main__':
    parse_email_to_wide.make()
    to_terms.make()
    to_dictionary.make()
    to_trimmed_dictionary.make()
    to_periods.make()
    to_corpora.make()
    to_lda.make()
    to_ldavis.make()
