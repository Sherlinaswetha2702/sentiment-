import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

def authenticate_twitter():
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    api = tweepy.API(auth)
    return api

def get_tweet_text(keyword, count=10):
    api = authenticate_twitter()
    tweets = api.search(q=keyword, count=count, lang='en')
    tweet_texts = [tweet.text for tweet in tweets]
    return tweet_texts

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return {'polarity': polarity, 'sentiment': sentiment}
