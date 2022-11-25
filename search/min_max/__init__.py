import math

from search import TrieSearch, TrieSearchUtils
from tree import VariationalNode, VariationalTrie


class CommonMinMaxUtils:
    @staticmethod
    def is_terminal(node: VariationalNode):
        return len(node.children) == 0 or all(child is None for child in node.children)

    @staticmethod
    def find_max(node: VariationalNode, *args):
        pass

    @staticmethod
    def find_min(node: VariationalNode, *args):
        pass


class GreedyMinMaxUtils(CommonMinMaxUtils):
    @staticmethod
    def find_max(node: VariationalNode, *args):
        max_value, max_child = -math.inf, None
        for child in node.children:
            if child is None:
                continue
            if max_value < child.value:
                max_value = child.value
                max_child = child
        return max_child

    @staticmethod
    def find_min(node: VariationalNode, *args):
        min_value, min_child = math.inf, None
        for child in node.children:
            if child is None:
                continue
            if min_value > child.value:
                min_value = child.value
                min_child = child
        return min_child


class GreedyMinMaxSearch(TrieSearch):
    def __init__(self, debug: bool = False):
        super(GreedyMinMaxSearch, self).__init__(debug)

    def search(self, trie: VariationalTrie):
        return self._search_max(trie.root)

    def _search_max(self, node: VariationalNode):
        if GreedyMinMaxUtils.is_terminal(node) or not TrieSearchUtils.is_memory_available():
            return node.value
        max_child = GreedyMinMaxUtils.find_max(node)
        if self._debug:
            print(f"Max: {max_child} from {node.children}")
        return self._search_min(max_child)

    def _search_min(self, node: VariationalNode):
        if GreedyMinMaxUtils.is_terminal(node) or not TrieSearchUtils.is_memory_available():
            return node.value
        min_child = GreedyMinMaxUtils.find_min(node)
        if self._debug:
            print(f"Min: {min_child} from {node.children}")
        return self._search_max(min_child)


class GreedyMinMaxIterativeDeepeningSearch(GreedyMinMaxSearch):
    def __init__(self, max_depth: int, debug: bool = False):
        super(GreedyMinMaxIterativeDeepeningSearch, self).__init__(debug)
        self._max_depth = max_depth

    def search(self, trie: VariationalTrie):
        value = 0
        depth = 0
        while True:
            if depth >= self._max_depth or not TrieSearchUtils.is_memory_available():
                return value
            value, is_terminal = self._search_max_deepening(trie.root, depth, 0)
            if is_terminal:
                return value
            depth += 1

    def _search_max_deepening(self, node: VariationalNode, max_depth: int, current_depth: int):
        if GreedyMinMaxUtils.is_terminal(node):
            return node.value, True
        if current_depth >= max_depth:
            return node.value, False
        max_child = GreedyMinMaxUtils.find_max(node)
        if self._debug:
            print(f"Max: {max_child} in {current_depth} from {node.children}")
        return self._search_min_deepening(max_child, max_depth, current_depth + 1)

    def _search_min_deepening(self, node: VariationalNode, max_depth: int, current_depth: int):
        if GreedyMinMaxUtils.is_terminal(node):
            return node.value, True
        if current_depth >= max_depth:
            return node.value, False
        min_child = GreedyMinMaxUtils.find_min(node)
        if self._debug:
            print(f"Min: {min_child} in {current_depth} from {node.children}")
        return self._search_max_deepening(min_child, max_depth, current_depth + 1)


class ClassicMinMaxUtils(CommonMinMaxUtils):
    @staticmethod
    def find_max(node: VariationalNode, *args):
        max_value = -math.inf
        for child in node.children:
            if child is None:
                continue
            min_recursive_func, *rest_recursive_func_args = args
            child_value = min_recursive_func(child, *rest_recursive_func_args)
            if max_value < child_value:
                max_value = child_value
        return max_value

    @staticmethod
    def find_min(node: VariationalNode, *args):
        min_value = +math.inf
        for child in node.children:
            if child is None:
                continue
            max_recursive_func, *rest_recursive_func_args = args
            child_value = max_recursive_func(child, *rest_recursive_func_args)
            if min_value > child_value:
                min_value = child_value
        return min_value


class ClassicMinMaxSearch(TrieSearch):
    def __init__(self, debug: bool = False):
        super(ClassicMinMaxSearch, self).__init__(debug)

    def search(self, trie: VariationalTrie):
        return self._search_max(trie.root)

    def _search_max(self, node: VariationalNode):
        if ClassicMinMaxUtils.is_terminal(node) or not TrieSearchUtils.is_memory_available():
            return node.value
        max_value = ClassicMinMaxUtils.find_max(node, self._search_min)
        if self._debug:
            print(f"Max: {max_value} from {node.children}")
        return max_value

    def _search_min(self, node: VariationalNode):
        if ClassicMinMaxUtils.is_terminal(node) or not TrieSearchUtils.is_memory_available():
            return node.value
        min_value = ClassicMinMaxUtils.find_min(node, self._search_max)
        if self._debug:
            print(f"Min: {min_value} from {node.children}")
        return min_value


class ClassicMinMaxIterativeDeepeningSearch(TrieSearch):
    def __init__(self, max_depth: int, debug: bool = False):
        super(ClassicMinMaxIterativeDeepeningSearch, self).__init__(debug)
        self._max_depth = max_depth

    def search(self, trie: VariationalTrie):
        value = 0
        depth = 0
        while True:
            if depth >= self._max_depth or not TrieSearchUtils.is_memory_available():
                return value
            value = self._search_max(trie.root, depth, 0)
            depth += 1

    def _search_max(self, node: VariationalNode, max_depth: int, current_depth: int):
        if ClassicMinMaxUtils.is_terminal(node) or current_depth >= max_depth:
            return node.value
        max_value = ClassicMinMaxUtils.find_max(node, self._search_min, max_depth, current_depth + 1)
        if self._debug:
            print(f"Max: {max_value} in {current_depth} from {node.children}")
        return max_value

    def _search_min(self, node: VariationalNode, max_depth: int, current_depth: int):
        if ClassicMinMaxUtils.is_terminal(node) or current_depth >= max_depth:
            return node.value
        min_value = ClassicMinMaxUtils.find_min(node, self._search_max, max_depth, current_depth + 1)
        if self._debug:
            print(f"Min: {min_value} in {current_depth} from {node.children}")
        return min_value
