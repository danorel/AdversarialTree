from search import TrieSearch
from tree import VariationalTrie


class AlphaBetaSearch(TrieSearch):
    def __init__(self, alpha: float, beta: float, debug: bool = False):
        super(AlphaBetaSearch, self).__init__(debug)
        self._alpha: float = alpha
        self._beta: float = beta

    def search(self, tree: VariationalTrie):
        return None
