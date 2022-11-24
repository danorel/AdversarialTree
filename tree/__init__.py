import math

from typing import Tuple, List
from random import random


class VariationalNode:
    def __init__(self, value: int):
        self.value = value
        self.children: List[VariationalNode] = []

    def __repr__(self):
        return f"Node: {self.value}"


class VariationalTrie:
    def __init__(self,
                 value_boundaries: Tuple[int, int],
                 branching_factor: Tuple[int, int],
                 depth: Tuple[int, int]):
        # Value boundaries
        self._value_boundaries = value_boundaries
        # Branching factor boundaries
        self._branching_factor = branching_factor
        # Depth of the search
        min_depth, max_depth = depth
        self._depth = min_depth + math.floor(random() * (max_depth - min_depth))
        # Tree itself
        self.root: VariationalNode or None = self._generate_deeply(None, 0)

    def _generate_deeply(self, node: VariationalNode or None, current_depth: int):
        if current_depth > self._depth:
            return None
        if node is None:
            min_value, max_value = self._value_boundaries
            value = min_value + math.floor(random() * (max_value - min_value))
            node = VariationalNode(value)
        min_branching_factor, max_branching_factor = self._branching_factor
        branching_factor = min_branching_factor + math.floor(random() * (max_branching_factor - min_branching_factor))
        for _ in range(branching_factor):
            child_node = self._generate_deeply(None, current_depth + 1)
            node.children.append(child_node)
        return node

    def __repr__(self):
        representation = f"depth = {self._depth + 1} \n"
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
            representation += ' ' * depth + f"{layer_size} branches\n"
            depth += 1
        return f"Tree: {representation}"
