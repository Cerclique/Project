# -*- encoding:Utf-8 -*-

#-----------------------------------------------------------------------------#
#   Author : VERNIZEAU Aurélien                                               #
#   File : data_processing.py                                                 #
#                                                                             #
#   Purpose : Process data collected by listener.py and store relevant        #
#             information in Excel file                                       #
#-----------------------------------------------------------------------------#

import json
import pandas as pd
import re
import time
###############  FUNCTION  ####################################################

# Function that extract link from relevant tweet
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

# Function to remove retweet from data collected
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return False
    return True

def get_date():
    return time.strftime("%d-%B-%Y-%H-%M-%S")

##############  CORE  #########################################################

# Define the path
data_file_path = 'data.txt'

# Open the data file
file = open(data_file_path, "r")

tweet_data = []

for line in file:
    try:
        data = json.loads(line)
        tweet_data.append(data)
    except:
        continue

# Create DataFrame
tweets = pd.DataFrame()
# Display untruncated information
pd.set_option('display.max_colwidth', -1)

# Get date of the tweet
tweets['date'] = map(lambda tweet: tweet['created_at'], tweet_data)
# Get pseudo
tweets['user'] = map(lambda tweet: tweet['user']['name'], tweet_data)
# Get username
tweets['screen_name'] = map(lambda tweet: tweet['user']['screen_name'], tweet_data)
# Get full text of the tweet
tweets['text'] = map(lambda tweet: tweet['text'], tweet_data)
# True if the tweet isn't a retweet of someone, Fale in the other case
tweets['rt'] = tweets['text'].apply(lambda tweet: word_in_text('RT @', tweet))
# Get link from text tweet if any
tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
# Remove all retweet from DataFrame
tweets = tweets[tweets.rt != False]

# Remove link from text for clearness
tweets['text'] = tweets['text'].replace(to_replace = tweets['link'], value= '', regex = True)

# Delete 'rt' column
tweets = tweets.drop('rt', 1)

# Re-index the entire DataFrame for clearness
tweets.reset_index(drop = True, inplace = True)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(get_date() + ".xlsx", engine='xlsxwriter')

# Convert the DataFrame to an Excel object
tweets.to_excel(writer, sheet_name=get_date())

# Close the Pandas Excel writer and output the Excel file.
writer.save()
