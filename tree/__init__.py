import math

from typing import Tuple, List
from random import random


class VariationalUtils:
    @staticmethod
    def generate_value(min_value: int, max_value: int):
        return min_value + math.floor(random() * (max_value - min_value))


class VariationalNode:
    def __init__(self, value: int, children=None):
        self.value = value
        self.children: List[VariationalNode] = [] if children is None else children

    def __repr__(self):
        return f"Node: {self.value}"


class VariationalTrie:
    def __init__(self,
                 value_boundaries: Tuple[int, int],
                 branching_factor: Tuple[int, int],
                 depth: Tuple[int, int],
                 debug: bool = False):
        self._debug = debug
        # Value boundaries
        self._value_boundaries = value_boundaries
        if self._debug:
            print(f"Initializing tree with value boundaries: {self._value_boundaries}")
        # Branching factor boundaries
        self._branching_factor = branching_factor
        if self._debug:
            print(f"Initializing tree with branching factors: {self._branching_factor}")
        # Depth of the search
        min_depth, max_depth = depth
        self._depth = VariationalUtils.generate_value(min_depth, max_depth)
        if self._debug:
            print(f"Initializing tree with depth: {self._depth}")
        # Tree itself
        self.root: VariationalNode or None = self._generate_deeply(None, 0)

    def _generate_deeply(self, node: VariationalNode or None, current_depth: int):
        if current_depth > self._depth:
            return None
        if node is None:
            min_value, max_value = self._value_boundaries
            value = VariationalUtils.generate_value(min_value, max_value)
            node = VariationalNode(value)
        min_branching_factor, max_branching_factor = self._branching_factor
        branching_factor = VariationalUtils.generate_value(min_branching_factor, max_branching_factor)
        for _ in range(branching_factor):
            child_node = self._generate_deeply(None, current_depth + 1)
            node.children.append(child_node)
        return node

    def __repr__(self):
        tree_size = 0
        tree_repr = f"depth = {self._depth + 1}\n"
        queue, depth = [self.root], 0
        while len(queue) > 0:
            size = len(queue)
            layer_size = 0
            while size > 0:
                node = queue.pop(0)
                for child in node.children:
                    if child is not None:
                        queue.append(child)
                layer_size += 1
                size -= 1
            layer_label = "node" if layer_size == 1 else "nodes"
            tree_repr += ' ' * depth + f"{layer_size} {layer_label}\n"
            depth += 1
            tree_size += layer_size
        tree_repr += f"Size: {tree_size} nodes"
        return f"Tree: {tree_repr}"
