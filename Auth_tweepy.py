import tweepy
from Conn.conn import conn as cnx


#4 cadenas para la autenticacion
consumer_key = "prXZBrf2PITPuWrFRrUd7Er63"
consumer_secret = "uY2p1BN9V0EMdnkJWuryB1jpWJypreqdu2VfPjMqZHg6fqvo7e"
access_token = "1568664902541123588-2mJjT9oZLza9X1w0ETG3Vt8Fax0x2y"
access_token_secret = "hCkCTiSNjylr6gtj3Kxm84aAAB6ReTmVCP0nZ0jJlJ0MH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth, wait_on_rate_limit=True)

conexion = cnx()
departments = conexion.get_departments()

try:
    for tweet in tweepy.Cursor(api.search_tweets, "Inseguridad",).items(50):
        if tweet.user.location in 'Atlántico, Colombia':
            print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at}')
            print(departments[1])
except Exception as e:
    print(e)
