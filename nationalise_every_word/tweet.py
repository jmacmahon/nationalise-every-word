from twitter import Api, TwitterError

from .config import config

api = Api(**config['keys'])


def write_tweet(word):
    tweet_body = config['format'].format(word)
    try:
        api.PostUpdate(tweet_body)
    except TwitterError as e:
        # Suppress duplicate tweet errors
        if e.message[0]['code'] != 187:
            raise
