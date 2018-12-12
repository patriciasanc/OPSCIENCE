#!/usr/bin/python
# encoding: utf-8


from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
from progressbar import ProgressBar, Percentage, Bar
import json
import sys

#Claves para el acceso al APP Twitter.
ckey="YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret="XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken="292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret="zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"


#The number of tweets we want to get
max_tweets=100

#Create the listener class that receives and saves tweets
class listener(StreamListener):

    #On init, set the counter to zero and create a progress bar
    def __init__(self, api=None):
        self.num_tweets = 0
        self.pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=max_tweets).start()

    #When data is received, do this
    def on_data(self, data):
        #Append the tweet to the 'tweets.txt' file
        with open('tweets3.txt', 'a') as tweet_file:
            tweet_file.write(data)
            #Increment the number of tweets
            self.num_tweets += 1
            #Check to see if we have hit max_tweets and exit if so
            if self.num_tweets >= max_tweets:
                self.pbar.finish()
                sys.exit(0)
            else:
                #increment the progress bar
                self.pbar.update(self.num_tweets)
        return True

    #Handle any errors that may occur
    def on_error(self, status):
        print status

#Autenticación en Twitter
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#Usar el listener class para el proceso en streaming
twitterStream = Stream(auth, listener())
#Filtrar por palabras clave (una o varias)
twitterStream.filter(track=["Ciencia"], languages=['es'])