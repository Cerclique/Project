# -*- coding:Utf-8 -*-

# Library use for stream listenning
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variable use to connect to Twitter API
consumer_key = "95mqN13a7dGLsGCxQEdcDN56V"
consumer_secret = "V9jHGwptqTVeEksIY4mwt31SXEIZykaQyfRPFrOqroX7WQj0AC"
access_token = "786739082-lE7EdD3kAHTdwwpAgBmEXmYXnp0yVUgxhv0n4lCG"
access_secret = "BpfPIjiQNHn24foz85D2vcDe4FWTCh315dL9iZ32njCUX"

# File that we will print collected tweet in
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

    # Connect to the API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, listener)

    # Filter to collect data from Twitter
    stream.filter(track=["3d printer", "3d printed", "3d printing", "impression 3d", u"imprimé 3d", "imprimante 3d"])
