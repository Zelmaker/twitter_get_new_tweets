# Twitter to Telegram

This project allows you to download all tweets from a specific Twitter account and send them to a Telegram chat. It uses the Tweepy library to retrieve tweets from Twitter and the python-telegram-bot library to send messages to Telegram.

## Requirements

- A Twitter developer account and API keys
- A Telegram bot and chat ID
- Python 3
- Tweepy library
- python-telegram-bot library

## Usage

1. Clone the repository
```bash
git clone https://github.com/Zelmaker/twitter_get_new_tweets.git
```

Install the required libraries
```
pip install tweepy python-telegram-bot
```

Replace the placeholders with your own Twitter API keys, Telegram bot token, and chat ID in the main.py file

Run the script

```
python main.py
```

## Functions

get_all_tweets(api, username): Retrieves all tweets from a specific Twitter account
watch_new_tweets(api, username, bot, chat_id): Watches for new tweets from a specific Twitter account and sends them to Telegram

## Note
Make sure that you're using the data ethically and legally, follow the Twitter API terms of service and developer agreement.
The script is a simplified example, it may require additional error handling and modification depending on the specific requirements of your project.

## Author
[Zelmaker](https://github.com/Zelmaker)
