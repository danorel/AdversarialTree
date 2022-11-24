import psutil

from tree import VariationalTrie


class TrieSearchUtils:
    @staticmethod
    def is_memory_available():
        left_virtual_memory_percentage = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
        return left_virtual_memory_percentage > 25


class TrieSearch:
    def __init__(self, debug: bool = False):
        self._debug = debug

    def search(self, tree: VariationalTrie):
        pass
