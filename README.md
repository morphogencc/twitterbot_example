# Example Twitterbot

An example twitterbot using python and tweepy.

## Requirements
- Python 2.7+
- tweepy

If you don't have tweepy, install it using `pip install tweepy`.

## Creating an App

Go to `http://apps.twitter.com` to create an application for your new bot.  You may wish to create a new account for
your bot so it doesn't spam your existing account while testing it!

Once you register your application, you can go to the `Settings` page and find your Consumer Key and Consumer Secret,
which you'll need to authorize yourself.  At the very bottom, under `Token Actions`, you can generate access tokens,
which you will also need.

## Connecting to Twitter

First, create a `config.json` file (it's already set in the `.gitignore` file so you don't accidentally commit it and post
it to the internet!).  The `config.json` file should take the following format:

```
{ 
    "consumer_key": "key",
    "consumer_secret": "secret",
    "access_token": "token",
    "access_token_secret": "token_secret"
}                                                                                                
```

Copy and paste your keys and tokens from your app's settings page.
