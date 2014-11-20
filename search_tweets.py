#!/use/bin/env python
#
# search_tweets.py
# nathan lachenmyer
# 2014 Nov
#
# Usage: python search_tweets.py [search query] [number of results]

import time
import sys
import json
import tweepy

config_file = open('config.json', 'r')
config_data = json.load(config_file)

CONSUMER_KEY = config_data['consumer_key']
CONSUMER_SECRET = config_data['consumer_secret']
ACCESS_TOKEN = config_data['access_token']
ACCESS_SECRET = config_data['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

search_query = sys.argv[1]
searched_tweets = []
last_id = -1
max_tweets = sys.argv[2]

#retrieve as many results as max_tweets indicates
while len(searched_tweets) < max_tweets:
    count = max_tweets - len(searched_tweets)
    try:
        new_tweets = api.search(q=search_query, count=count, max_id=str(last_id - 1))
        if not new_tweets:
            break
        searched_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        break
