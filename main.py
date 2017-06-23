#!/usr/bin/python3

from nationalise_every_word import words_gen, write_tweet, config

from time import sleep
from sys import exc_info
from traceback import format_exception

def run():
    for (word_index, word) in words_gen():
        try:
            write_tweet(word)
            print('Tweeted word: {}'.format(word))
        except Exception as e:
            message = ('Caught an exception on word {} ' +
                'at index {}:'.format(word, word_index))
            log = format_exception(*sys.exc_info())
            with open(config['error_log'], 'a') as error_log:
                error_log.writelines((message, log))
            print((message, log))
        finally:
            sleep(config['interval'])

if __name__ == "__main__":
    run()
