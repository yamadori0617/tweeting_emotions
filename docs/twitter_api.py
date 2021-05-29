import re
import tweepy
import configparser


config = configparser.ConfigParser()
config.read('../config.ini', encoding="utf-8")

API_KEY = config.get('API_INFO', 'API_KEY')
API_SECRET = config.get('API_INFO', 'API_SECRET')
ACCESS_TOKEN = config.get('API_INFO', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config.get('API_INFO', 'ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)


def get_tweets(keyword: str, count: int) -> list:
    tweets = []
    query = re.sub('[<>/\\\'\"\t\n]', '', keyword)+' exclude:retweets AND exclude:retweets'
    api.search(q=query, count=count, tweet_mode='extended', exclude_replies='True')
    for tweet in tweepy.Cursor(api.search, q=query, tweet_mode='extended', exclude_replies='True', lang='ja').items(count):
        tweets.append(tweet)
    return tweets


def print_tweets_text(tweets: list) -> None:
    for tweet in tweets:
        print(tweet.full_text)
        print("--------------------------------------------")


def main():
    try:
        query = input("keyword: ")
        count = int(input("count: "))
        print()

        tweets = get_tweets(query, count)
        print_tweets_text(tweets)

    except ValueError as e:
        print('Enter an integer for count.')

    except tweepy.TweepError as e:
        print('The API token may be wrong.')


if __name__ == "__main__":
    main()
