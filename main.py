#!/usr/bin/env python3

from nationalise_every_word import words_gen, write_tweet, config

from time import sleep
from sys import exc_info
from traceback import format_exception
from urllib3.exceptions import MaxRetryError


def run():
    for (word_index, word) in words_gen():
        success = False
        while not success:
            try:
                write_tweet(word)
                print('Tweeted word: {}'.format(word))
                success = True
            except MaxRetryError:
                sleep(config['interval'])
            except Exception as e:
                message = ('Caught an exception on word {} ' +
                           'at index {}:').format(word, word_index)
                log = format_exception(*exc_info())
                with open(config['error_log'], 'a') as error_log:
                    error_log.writelines((message, log))
                print((message, log))
        sleep(config['interval'])


if __name__ == "__main__":
    run()
