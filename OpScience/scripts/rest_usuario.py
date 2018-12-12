#!/usr/bin/env python
# encoding: utf-8
#Este script descarga los tweets sin parsear de un usuario determinado usando API REST
#IMPRIME LOS RESULTADOS A UN ARCHIVO CSV

import tweepy
import csv

#Acceso APP Twitter
ckey="YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret="XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken="292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret="zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"

def get_all_tweets(screen_name):

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #escribe un csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    pass

if __name__ == '__main__':
# Filtrar por el nombre de usuario de la cuenta que queremos descargar mensajes:
    get_all_tweets("materia_ciencia")
