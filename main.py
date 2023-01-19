import tweepy
import json
from telegram import Bot
from telegram import Update

def get_all_tweets(api, username):
    """Retrieve all tweets from a specific Twitter account"""
    # Initialize a list to hold all the tweets
    all_tweets = []

    # Get the first 200 tweets from the account
    tweets = api.user_timeline(screen_name=username, count=200)
    all_tweets.extend(tweets)

    # Keep track of the oldest tweet
    oldest_tweet = all_tweets[-1].id - 1

    # Retrieve additional tweets until there are no more tweets to retrieve
    while len(tweets) > 0:
        tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest_tweet)
        all_tweets.extend(tweets)
        oldest_tweet = all_tweets[-1].id - 1

    return all_tweets

def watch_new_tweets(api, username, bot, chat_id):
    """Watch for new tweets from a specific Twitter account and send them to Telegram"""
    # Get the last tweet from the account
    last_tweet = api.user_timeline(screen_name=username, count=1)[0]

    while True:
        # Check for new tweets
        tweets = api.user_timeline(screen_name=username, count=1, since_id=last_tweet.id)

        # If there are new tweets, send them to Telegram
        if len(tweets) > 0:
            for tweet in tweets:
                message = f"New tweet from @{username}: {tweet.text}"
                bot.send_message(chat_id=chat_id, text=message)
                last_tweet = tweet
        
        time.sleep(60) # wait for 60 seconds before checking for new tweets again

# Authentication
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_secret = "YOUR_ACCESS_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Telegram bot
bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
chat_id = "YOUR_CHAT_ID"

# Retrieve all tweets from the account
tweets = get_all_tweets(api, "twitter_username")

# Send all tweets to Telegram
for tweet in tweets:
    message = f"Tweet from @{username}: {tweet.text}"
    bot.send_message(chat_id=chat_id, text=message)

# Watch for new tweets
watch_new_tweets(api, "twitter_username",bot, chat_id)
