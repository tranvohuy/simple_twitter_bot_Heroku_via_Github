import time
import sys
import tweepy
import datetime

#from local_settings import *  # use this one for testing

# use this for production; set vars in heroku dashboard
from os import environ
Consumer_key = environ['Consumer_key']
Consumer_secret = environ['Consumer_secret']
Access_key = environ['Access_key']
Access_secret = environ['Access_secret']

#INTERVAL = 60 * 60 * 6  # tweet every 6 hours
#INTERVAL = 60  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_key, Access_secret)
api = tweepy.API(auth)

if __name__ == '__main__':
    print("about to update status...")
    api.update_status('This bot is deployed via  Heroku dashboard connecting to Github. Right now the time is ' + str(datetime.datetime.now()))
 #   time.sleep(INTERVAL)
