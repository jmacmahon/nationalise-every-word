from .config import config
from json import load, dump
from copy import deepcopy
from contextlib import contextmanager

class Store(object):
    def __init__(self, store_file, defaults):
        self._store_file = store_file
        try:
            with open(store_file, 'r') as store_file:
                self._store = load(store_file)
        except FileNotFoundError:
            self._store = deepcopy(defaults)
            self._write_store()

    def _write_store(self):
        with open(self._store_file, 'w') as store_file:
            dump(self._store, store_file)

    def get(self, key):
        return deepcopy(self._store[key])

    def set(self, key, value):
        self._store[key] = value
        self._write_store()


with open(config['words_file'], 'r') as words_file:
    words = words_file.readlines()


store = Store(config['store_file'], {'latest_index': 0})

@contextmanager
def pop_word():
    latest_index = store.get('latest_index')
    yield latest_index, words[latest_index % len(words)]
    store.set('latest_index', latest_index + 1)

def words_gen():
    with pop_word() as (index, word):
        yield index, word
