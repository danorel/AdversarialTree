import math
import psutil

from search import TrieSearch
from tree import VariationalNode, VariationalTrie


class GreedyMinMaxUtils:
    @staticmethod
    def find_max(node: VariationalNode):
        if node is None:
            return None
        max_value, max_child = -math.inf, None
        for child in node.children:
            if child is None:
                continue
            if max_value < child.value:
                max_value = child.value
                max_child = child
        if max_child is None:
            return node
        return max_child

    @staticmethod
    def find_min(node: VariationalNode):
        if node is None:
            return None
        min_value, min_child = math.inf, None
        for child in node.children:
            if child is None:
                continue
            if min_value > child.value:
                min_value = child.value
                min_child = child
        return min_child


class GreedyMinMaxSearch(TrieSearch):
    def __init__(self, debug: bool = True):
        super(GreedyMinMaxSearch, self).__init__(debug)

    def search(self, trie: VariationalTrie):
        return self._search_max(trie.root)

    def _search_max(self, node: VariationalNode):
        max_child = GreedyMinMaxUtils.find_max(node)
        if max_child is None:
            return node.value
        if self._debug:
            print(f"Max: {max_child} from {node.children}")
        return self._search_min(max_child)

    def _search_min(self, node: VariationalNode):
        min_child = GreedyMinMaxUtils.find_min(node)
        if min_child is None:
            return node.value
        if self._debug:
            print(f"Min: {min_child} from {node.children}")
        return self._search_max(min_child)


class GreedyMinMaxIterativeDeepeningSearch(GreedyMinMaxSearch):
    def __init__(self, debug: bool = True):
        super(GreedyMinMaxIterativeDeepeningSearch, self).__init__(debug)

    def search(self, trie: VariationalTrie):
        last_value = 0
        depth = 0
        while True:
            memory_percentage = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
            if memory_percentage < 25:
                return last_value
            last_value, is_leaf = self._search_max_deepening(trie.root, depth, 0)
            if is_leaf:
                return last_value
            depth += 1

    def _search_max_deepening(self, node: VariationalNode, max_depth: int, current_depth: int):
        if current_depth >= max_depth:
            return node.value, False
        max_child = GreedyMinMaxUtils.find_max(node)
        if max_child is None:
            return node.value, True
        if self._debug:
            print(f"Max: {max_child} in {current_depth} from {node.children}")
        return self._search_min_deepening(max_child, max_depth, current_depth + 1)

    def _search_min_deepening(self, node: VariationalNode, max_depth: int, current_depth: int):
        if current_depth >= max_depth:
            return node.value, False
        min_child = GreedyMinMaxUtils.find_min(node)
        if min_child is None:
            return node.value, True
        if self._debug:
            print(f"Min: {min_child} in {current_depth} from {node.children}")
        return self._search_max_deepening(min_child, max_depth, current_depth + 1)


class MinMaxSearch(TrieSearch):
    def __init__(self, debug: bool = True):
        super(MinMaxSearch, self).__init__(debug)

    def search(self, trie: VariationalTrie):
        return self._search_max(trie.root)

    def _search_max(self, node: VariationalNode):
        max_value, max_node = -math.inf, None
        for child in node.children:
            if child is None:
                continue
            child_value, child_node = self._search_min(child)
            if child_node is None:
                continue
            if max_value < child_value:
                max_value = child_value
                max_node = child_node
        if self._debug:
            print(f"Max: {max_value} from {node.children}")
        return max_value, max_node

    def _search_min(self, node: VariationalNode):
        min_value, min_node = +math.inf, None
        for child in node.children:
            if child is None:
                continue
            child_value, child_node = self._search_max(child)
            if child_node is None:
                continue
            if min_value > child_value:
                min_value = child_value
                min_node = child_node
        if self._debug:
            print(f"Min: {min_value} from {node.children}")
        return min_value, min_node
