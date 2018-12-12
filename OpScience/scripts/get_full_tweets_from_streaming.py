#!/usr/bin/env python
# encoding: utf-8
# Este Script se conecta al Streaming de Twitter y descarga los tweets PARSEADOS SIN RT Y LOS FULL TWEETS EN CASO DE ESTAR TRUNCADOS en formato Json que contengan en el texto una palabra como por ejemplo "#ciencia"

# IMPRIME solo las partes del tweet que le pidamos, por ejemplo "text".
# Correr desde consola con Python2 y se muestran los resultados por la misma consola.


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

#consumer key, consumer secret, access token, access secret.
ckey="YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret="XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken="292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret="zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"

class listener(StreamListener):
    def on_status(self, status):
        if not status.retweeted and 'RT @' not in status.text:
            try:
                tweet = status.extended_tweet['full_text']
            except AttributeError:
                tweet = status.text

            print tweet
        else:
            return

#Autenticación en Twitter
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#Usar el listener class para el proceso en streaming
twitterStream = Stream(auth, listener())
#Filtrar por palabras clave (una o varias)
twitterStream.filter(track=["Ciencia"])
