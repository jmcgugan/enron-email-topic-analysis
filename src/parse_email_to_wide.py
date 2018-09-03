import numpy as np
import pandas as pd
import email

def make():
    parse_email_to_wide('../data/emails.csv', '../data/emails_wide.csv')

## Helper functions
def get_text_from_email(msg):
  '''To get the content from email objects'''
  parts = []
  for part in msg.walk():
      if part.get_content_type() == 'text/plain':
          parts.append( part.get_payload() )
  return ''.join(parts)

def split_email_addresses(line):
  '''To separate multiple email addresses'''
  return line # do not need anything more complicated for now
  if line:
      addrs = line.split(',')
      addrs = frozenset(map(lambda x: x.strip(), addrs))
  else:
      addrs = None
  return addrs

def parse_email_to_wide(infilename, outfilename):
  '''Parse email body to separate parts stored in dataframe columns.
  Write new wide dataframe to outfilename.
  '''
  # Parse the emails into a list email objects
  emails_df = pd.read_csv(infilename) # just 2 columns
  messages = list(map(email.message_from_string, emails_df['message']))
  emails_df.drop('message', axis=1, inplace=True) # because it is big
  # Get fields from parsed email objects
  keys = messages[0].keys()
  for key in keys:
    emails_df[key] = [doc[key] for doc in messages]
  # Parse content from emails
  emails_df['content'] = list(map(get_text_from_email, messages))
  # Split multiple email addresses
  emails_df['From'] = emails_df['From'].map(split_email_addresses)
  emails_df['To'] = emails_df['To'].map(split_email_addresses)

  # Extract the root of 'file' as 'user'
  emails_df['user'] = emails_df['file'].map(lambda x:x.split('/')[0])
  del messages

  # Set index and drop columns with two few values
  emails_df = emails_df.drop(['file', 'Mime-Version', 'Content-Type', 'Content-Transfer-Encoding'], axis=1)
  # Parse datetime
  emails_df['Date'] = pd.to_datetime(emails_df['Date'], infer_datetime_format=True)
  #emails_df = emails_df.set_index('Date')
  emails_df.sort_values('Date').to_csv(outfilename)


if __name__ == '__main__':
    make()
