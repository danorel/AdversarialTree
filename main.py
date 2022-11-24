import math

from typing import List

from tree import VariationalTrie
from search import AlphaBetaSearch, MinMaxSearch, MinMaxIterativeDeepeningSearch, TrieSearch


def comparator(search_algorithms: List[TrieSearch]):
    trie = VariationalTrie(
        value_boundaries=(1, 100),
        branching_factor=(1, 5),
        depth=(10, 15)
    )
    print(trie)
    for search_algorithm in search_algorithms:
        print(f"{search_algorithm.__class__}: {search_algorithm.search(trie)}")


def main():
    comparator([
        MinMaxSearch(),
        MinMaxIterativeDeepeningSearch(),
        AlphaBetaSearch(
            alpha=math.inf,
            beta=+math.inf
        )
    ])


if __name__ == '__main__':
    main()
