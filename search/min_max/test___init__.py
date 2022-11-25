from unittest import TestCase

from tree import VariationalTrie, VariationalNode
from search.min_max import ClassicMinMaxSearch


class TestClassicMinMaxSearch(TestCase):
    def setUp(self):
        self.algorithm = ClassicMinMaxSearch()
        self.trie = VariationalTrie(
            branching_factor=(1, 2),
            value_boundaries=(1, 100),
            depth=(3, 3)
        )
        self.trie.root = VariationalNode(
            value=3,
            children=[
                VariationalNode(
                    value=3,
                    children=[
                        VariationalNode(value=3),
                        VariationalNode(value=12),
                        VariationalNode(value=8)
                    ]
                ),
                VariationalNode(
                    value=2,
                    children=[
                        VariationalNode(value=2),
                        VariationalNode(value=4),
                        VariationalNode(value=6)
                    ]
                ),
                VariationalNode(
                    value=2,
                    children=[
                        VariationalNode(value=14),
                        VariationalNode(value=5),
                        VariationalNode(value=2)
                    ]
                )
            ]
        )

    def test_search(self):
        self.failUnlessEqual(self.algorithm.search(self.trie), 3)
