#!/use/bin/env python
#
# search_tweets.py
# nathan lachenmyer
# 2017 March
#
# Usage: python search_tweets.py [search query] [number of results]
import sys
import json
import tweepy

config_file = open('config.json', 'r')
config_data = json.load(config_file)

CONSUMER_KEY = config_data['consumer_key']
CONSUMER_SECRET = config_data['consumer_secret']
ACCESS_TOKEN = config_data['access_token']
ACCESS_SECRET = config_data['access_token_secret']

# Uncomment if you want to use User Authorization, but comment out Application Authroization below!
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Using Application Authorization so we get a higher rate limit of 450 queries / 15 minutes
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
    print ("ERROR : Problem connecting to API")

search_query = sys.argv[1]

searched_tweets = []
last_id = -1

if len(sys.argv) >= 3:
    max_tweets = int(sys.argv[2])
else:
    max_tweets = 25

for tweet in tweepy.Cursor(api.search,q=search_query).items(max_tweets):
    print("{0} tweeted {1}".format(tweet.user.screen_name, tweet.text.encode('utf-8')))
