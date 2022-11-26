import math

from search import TrieSearch
from tree import VariationalTrie, VariationalNode
from utils import time_it


class ClassicAlphaBetaUtils:
    @staticmethod
    def is_terminal(node: VariationalNode):
        return len(node.children) == 0 or all(child is None for child in node.children)


class ClassicAlphaBetaSearch(TrieSearch):
    def __init__(self, debug: bool = False):
        super(ClassicAlphaBetaSearch, self).__init__(debug)

    @time_it()
    def search(self, tree: VariationalTrie):
        return self._search_max(tree.root, -math.inf, +math.inf)

    def _search_max(self, node: VariationalNode, alpha: float, beta: float):
        if ClassicAlphaBetaUtils.is_terminal(node):
            return node.value
        max_value = -math.inf
        for child in node.children:
            child_value = self._search_min(child, alpha, beta)
            if max_value < child_value:
                max_value = child_value
                if alpha < max_value:
                    alpha = max_value
            if max_value >= beta:
                return max_value
        return max_value

    def _search_min(self, node: VariationalNode, alpha: float, beta: float):
        if ClassicAlphaBetaUtils.is_terminal(node):
            return node.value
        min_value = +math.inf
        for child in node.children:
            child_value = self._search_max(child, alpha, beta)
            if min_value > child_value:
                min_value = child_value
                if beta > min_value:
                    beta = min_value
            if min_value <= alpha:
                return min_value
        return min_value
