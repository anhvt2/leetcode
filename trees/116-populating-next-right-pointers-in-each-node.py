from typing import List, Optional
from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Convert a tree node to a linked list
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = deque([root])
        while q:
            prev = None
            # process one level at a time
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # end of this level -> last node's next should already be None
            prev.next = None

        return root
