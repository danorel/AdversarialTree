import math

from typing import List

from search import TrieSearch
from search.alpha_beta import AlphaBetaSearch
from search.min_max import \
    GreedyMinMaxSearch, \
    GreedyMinMaxIterativeDeepeningSearch, \
    ClassicMinMaxSearch, \
    ClassicMinMaxIterativeDeepeningSearch
from tree import VariationalTrie


def comparator(search_algorithms: List[TrieSearch]):
    trie = VariationalTrie(
        value_boundaries=(1, 100),
        branching_factor=(1, 4),
        depth=(15, 17),
        debug=True
    )
    print(trie)
    for search_algorithm in search_algorithms:
        print(f"{search_algorithm.__class__}: {search_algorithm.search(trie)}")


def main():
    comparator([
        GreedyMinMaxSearch(),
        GreedyMinMaxIterativeDeepeningSearch(
            max_depth=20
        ),
        ClassicMinMaxSearch(),
        ClassicMinMaxIterativeDeepeningSearch(
            max_depth=20
        ),
        AlphaBetaSearch(
            alpha=math.inf,
            beta=+math.inf
        )
    ])


if __name__ == '__main__':
    main()
