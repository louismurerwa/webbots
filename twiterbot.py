#the bot
import tweepy as tp
import Tkinter
import time
import os

#credidentials
access_token ='992516614087159808-PwwohArdfhcW8NJgzUGtA7PtIZBQzwa'
access_secret =	'FLGFeoAGyh22GMz9jAYgvC2JjLCVPPhajLiqAWyb270yC'
consumer_key = 'wHmzwq9nEhgVfYexKkiPkMfOl'
consumer_secret = 'Q1Rqe6kUx2KGYfWmmvg6vJVWUNX0ySWkZxEcWJlJvGZ0XMzPk5'

# log in to twite

auth = tp.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

#iterates over pictures in image folder

os.chdir('models')
for model_image in os.listdir('.'):
	api.update_with_media(model_image)
	time.sleep(3)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)