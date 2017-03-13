#!/use/bin/env python
#
# send_tweet.py
# nathan lachenmyer
# 2014 Nov
#
# Usage: python search_tweets.py [text to tweet]

import tweepy
import time
import sys
import json

config_file = open('config.json', 'r')
config_data = json.load(config_file)

CONSUMER_KEY = config_data['consumer_key']
CONSUMER_SECRET = config_data['consumer_secret']
ACCESS_TOKEN = config_data['access_token']
ACCESS_SECRET = config_data['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("hello world!")

