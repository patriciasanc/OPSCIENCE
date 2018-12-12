#!/usr/bin/env python
# encoding: utf-8
# Este Script se conecta al API Streaming de Twitter y descarga los tweets PARSEADOS en formato Json que contengan en el texto una palabra, como por ejemplo "#Ciencia".
# IMPRIME solo las partes del tweet que le pidamos, en este caso "created at", "text" y "user".
# Correr desde consola con Python2 y se muestran los resultados por la misma consola.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time

#Claves para el acceso al API Twitter. consumer key, consumer secret, access token, access secret.
ckey="YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret="XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken="292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret="zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"

# Crear la clase que recibe y guarda los tweets.
class listener(StreamListener):

    def on_data(self, data):
	
        all_data = json.loads(data)
        # Si quisieramos que imprima el campo de time, debemos crear la variable:
        time = all_data["created_at"]
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]

        print((tweet))
        # Para pedir que la imprima con más información de variables:
        # print((time,username,tweet))
        
	
        return True
    
    def on_error(self, status):
        print status

#Autenticación en Twitter
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#Usar el listener class para el proceso en streaming
twitterStream = Stream(auth, listener())
#Filtrar por palabras clave (una o varias)
twitterStream.filter(track=["Ciencia"])
