#-----------------------------------------------------------------------------#
#   File : listener.py                                                        #
#                                                                             #
#   Purpose : Collect relevant tweet using Twitter API and Tweepy library     #
#             Store them into text file for later processing                  #
#-----------------------------------------------------------------------------#

# -*- coding:Utf-8 -*-

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variable use to connect to Twitter API
consumer_key = "QNGoTRr1KglswApSQDB8k6R5z"
consumer_secret = "7s8N5gS09aebqNCrSBm7lskzUfD1Vz9rxqW3d9kJsxBOpbxCgm"
access_token = "826541604316053504-XVag5sKqfW0rCde6Mq9jqiKuvDQoAZq"
access_secret = "a6zp37nJjfq1rumB8eulYMQS25JtfiuAmDT9EZT0XYZD6"

# File that will contain collected tweet
path = 'data.txt'
file = open(path, "w")

# Class to deal with tweet/error while collecting
class Listener(StreamListener):

    def on_data(self, data):
        file.write(data)
        return True

    def on_error(self, status):
        print status
        file.close()

if __name__ == '__main__':

    listener = Listener()

    # Connect to Twitter API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, listener)

    # Filter to collect data from Twitter
    stream.filter(track=["3d printer", "3d printed", "3d printing", "impression 3d", u"imprimé 3d", "imprimante 3d"])
