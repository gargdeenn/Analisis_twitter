# from datetime import date, datetime
# from Conn.conn import conn as cnx  
# import tweepy
# from Models.tweet import tweet as tuit

# #4 cadenas para la autenticacion
# consumer_key = "prXZBrf2PITPuWrFRrUd7Er63"
# consumer_secret = "uY2p1BN9V0EMdnkJWuryB1jpWJypreqdu2VfPjMqZHg6fqvo7e"
# access_token = "1568664902541123588-2mJjT9oZLza9X1w0ETG3Vt8Fax0x2y"
# access_token_secret = "hCkCTiSNjylr6gtj3Kxm84aAAB6ReTmVCP0nZ0jJlJ0MH"
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# #con este objeto realizaremos todas las llamadas al API
# api = tweepy.API(auth, wait_on_rate_limit=True)

# conexion = cnx()
# i=0
# fecha: datetime
# Tweets=[]

# try:
#     for tweet in tweepy.Cursor(api.search_tweets, f"inseguridad",geocode="10.46264,-73.26144,15mi").items(60):
#         fecha = tweet.created_at
#         print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at} - Ubicación: {tweet.user.location}')
#         i=i+1
#         Tweet= tuit(fecha.day,fecha.month,fecha.year,'inseguridad','1')
#         Tweets.append(Tweet)
#     conexion.post_Tweets(Tweets)
# except Exception as e:
#     print(e)
# try:
#     for tweet in tweepy.Cursor(api.search_tweets, f"inseguridad",geocode="10.85593,-74.83383,15mi").items(402):
#         fecha = tweet.created_at
#         print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at} - Ubicación: {tweet.user.location}')
#         i=i+1
#         Tweet= tuit(fecha.day,fecha.month,fecha.year,'corrupción','2')
#         Tweets.append(Tweet)
#     conexion.post_Tweets(Tweets)
# except Exception as e:    
#     print(e)
# try:
#     for tweet in tweepy.Cursor(api.search_tweets, f"corrupción",geocode="3.42562,-76.44192,15mi").items(752):
#         fecha = tweet.created_at
#         print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at} - Ubicación: {tweet.user.location}')
#         i=i+1
#         Tweet= tuit(fecha.day,fecha.month,fecha.year,'corrupción','3')
#         Tweets.append(Tweet)
#     conexion.post_Tweets(Tweets)
# except Exception as e:
#     print(e)
# try:
#     for tweet in tweepy.Cursor(api.search_tweets, f"corrupción",geocode="4.66266,-74.09180,15mi").items(52):
#         fecha = tweet.created_at
#         print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at} - Ubicación: {tweet.user.location}')
#         i=i+1
#         Tweet= tuit(fecha.day,fecha.month,fecha.year,'corrupción','4')
#         Tweets.append(Tweet)
#     conexion.post_Tweets(Tweets)
# except Exception as e:
#     print(e)
# try:
#     for tweet in tweepy.Cursor(api.search_tweets, f"corrupción",geocode="6.22853,-75.58252,15mi").items(882):
#         fecha = tweet.created_at
#         print(f'Usuario: {tweet.user.screen_name} - Tweet: {tweet.text} - Fecha creación: {tweet.created_at} - Ubicación: {tweet.user.location}')
#         i=i+1
#         Tweet= tuit(fecha.day,fecha.month,fecha.year,'corrupción','5')
#         Tweets.append(Tweet)
#     conexion.post_Tweets(Tweets)
# except Exception as e:
#     print(e)
# print(i)
