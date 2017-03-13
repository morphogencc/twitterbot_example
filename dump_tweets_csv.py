#!/use/bin/env python
#
# dump_tweets.py
# nathan lachenmyer
# 2017 March
#
# Usage: python dump_tweets.py [twitter username]

import time
import sys
import json
import tweepy
import csv

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

username = sys.argv[1]

alltweets = []	
new_tweets = api.user_timeline(screen_name=username,count=450)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1

while len(new_tweets) > 0:
        print("Retrieving tweets before {}".format(oldest))
        new_tweets = api.user_timeline(screen_name=username,count=450,max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print("...{0} tweets downloaded so far".format(len(alltweets)))

outtweets = [[tweet.id_str, tweet.created_at, "{0}".format(tweet.text)] for tweet in alltweets]

#write the csv	
with open("{}_tweets.csv".format(username), 'w', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
