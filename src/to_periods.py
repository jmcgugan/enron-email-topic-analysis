import numpy as np
import pandas as pd
import datetime

def load(infilename):
    '''
    Read wide dataframe from pickle file from infilename & return a dataframe sorted by Date.
    '''
    emails = pd.read_pickle(infilename)
    emails['Date'] = pd.to_datetime(emails['Date'], infer_datetime_format=True)
    emails = emails.sort_values('Date')
    return emails

def get_periods():
    '''Return a sorted list of datetime pairs representing consecutive periods.
    Note: this code currently only returns one month periods between Jan 1 2000
    and Dec 31 2001, roughly matching the Enron corpus' duration. The idea is
    to eventually generalize it to other period types like week and quarter.
    '''
    periods = []
    for year in range(2000,2002):
        for month in range(1,13):
            start = datetime.datetime(year,month,1,0,0,0)
            if month in {1,3,5,7,8,10,12}:
                last_day = 31
            elif (month == 2):
                if (year % 4) == 0:
                    last_day = 29
                else:
                    last_day = 28
            else:
                last_day = 30
            end = datetime.datetime(year,month,last_day,23,59,59)
            periods.append( (start, end) )
    return periods

def make_periods(infilename, outdir, dates=None):
    '''
    Read the full emails_wide-terms file from infilename, break it up on one
    month boundaries, and write each month of data out into a separate file.
    The output files are identical to the input file other than for each
    containing only one calendar month of data from the original file. All the
    output files are written into outdir with filenames derived from the period
    they represent.

    Note that if the optional dates parameter is is supplied, you can override
    the default one month periods. If the dates param is populated, it should
    look like [ (starttime, endtime), (anotherstart, anotherend), etc.]
    '''
    emails_df = load(infilename)
    if dates == None:
        periods = get_periods()
    else:
        periods = dates
    for start, end in periods:
        emails_for_period = \
            emails_df[ (emails_df['Date'] >= start) & (emails_df['Date'] <= end)]
        year_str = str(start.year)
        month_str = str(start.month)
        if len(month_str) == 1:
            month_str = '0'+month_str
        outfile = outdir + '/' + year_str + '-' + month_str + '.pkl'
        emails_for_period.to_pickle(outfile)

def make():
    make_periods('../data/emails_wide_terms.pkl', '../data/periods')

if __name__ == '__main__':
    make()
