#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Descarga los tweets del API streaming de Twitter filtrando por palabra o palabras clave.
# Muestra por pantalla el mensaje con su sentimiento (positivo o negativo) y el intervalo de confianza de ese sentimiento (0-1).
# Escribe y almacena en un archivo .txt los sentimientos de los mensajes que han obtenido una confianza de al menos .80


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

# consumer key, consumer secret, access token, access secret.
ckey = "YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret = "XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken = "292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret = "zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        tweet.encode('utf-8', 'ignore')
        print(tweet, sentiment_value, confidence)

        if confidence * 100 >= 80:
            output = open("twitter-out.txt", "a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ciencia"], languages=['es'])
