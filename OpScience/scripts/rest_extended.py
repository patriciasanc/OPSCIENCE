#Este script descarga los tweets con un determinado contenido en el texto del mensaje usando API REST de Twitter.

import tweepy

#Claves del app Twitter
ckey="YVTFs7SEBVl8GflMSFGj5YCwJ"
csecret="XahHa3xOvcAZcTko1L9wP8IRsRol2U9sBDGCmz2Cis1vwjSxLn"
atoken="292230217-G9rGK5cqj6SOnqfmvHC5bceCwr4JgkUbyDWt8sjh"
asecret="zQabuIlsmKhBDQwULFEQ3bSKGiZgWrgJObIMDoqNFVzFh"

#Autenticación
OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

# Aqui se indica el texto dentro del tweet que se quiera buscar y las fechas:
cricTweet = tweepy.Cursor(api.search, q='ciencia', exclude= "retweets", lang="es", tweet_mode='extended').items()

for tweet in cricTweet:
    #Para imprimir fecha y texto.
    #print tweet.created_at, tweet.full_text

    #Imprimir texto completo sin fecha:
    print tweet.full_text
