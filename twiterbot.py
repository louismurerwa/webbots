#the bot
import tweepy as tp
import Tkinter
import time
import os

#credidentials


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
