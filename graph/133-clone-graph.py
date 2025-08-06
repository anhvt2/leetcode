"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case
        if not node:
            return None
        
        # Map from original node (key) to cloned node (value)
        old2new = {}

        def dfs(n: 'Node') -> 'Node':
            # if we have already cloned this node, return its clone
            if n in old2new:
                return old2new[n]

            # (1)) Clone it `n` -> `copy``
            copy = Node(n.val)
            old2new[n] = copy

            # (2) Recursively clone and attach all neighbors
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei)) # not n.nei, but propagate throughout the graph recursively
            
            return copy
        return dfs(node)