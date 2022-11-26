from typing import List

from search import TrieSearch
from search.alpha_beta import ClassicAlphaBetaSearch
from search.min_max import \
    GreedyMinMaxSearch, \
    GreedyMinMaxIterativeDeepeningSearch, \
    ClassicMinMaxSearch, \
    ClassicMinMaxIterativeDeepeningSearch
from tree import VariationalTrie


def comparator(search_algorithms: List[TrieSearch]):
    trie = VariationalTrie(
        value_boundaries=(1, 100),
        branching_factor=(30, 35),
        depth=(3, 5),
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
        ClassicAlphaBetaSearch()
    ])


if __name__ == '__main__':
    main()
