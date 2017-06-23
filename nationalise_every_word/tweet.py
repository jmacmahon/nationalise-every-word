from twitter import Api, TwitterError

from .config import config

api = Api(**config['keys'])


def write_tweet(word):
    tweet_body = config['format'].format(word)
    api.PostUpdate(tweet_body)
