# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
from typing import Optional, List

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Ideas:
        # Perform a BFS (level-order) to ensure top-to-bottom order
        # Track horizontal column index for each node
        #   Root @ col=0
        #   Left child @ col-1
        #   Right child @ col+1
        # Group values by column into dictionary
        # Sort columns from left to right
        if not root:
            return []

        # col -> list of nodes in that column
        col_table = defaultdict(list)
        queue = deque([(root, 0)]) # (node, column)

        min_col = max_col = 0
        while queue:
            node, col = queue.popleft()
            if node:
                col_table[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)

                queue.append((node.left, col-1))
                queue.append((node.right, col+1))

        # collect result from min_col to max_col
        return [col_table[c] for c in range(min_col, max_col+1)]
