from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# # ---- First Solution: DFS
# class Solution:
#     def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
        
#         nodes = [] # list of (col, row, val)

#         def dfs(node: Optional[TreeNode], x: int, y:int) -> None:
#             # x: col, y, row
#             if not node:
#                 return
#             nodes.append((x, y, node.val))
#             dfs(node.left, x-1, y+1)
#             dfs(node.right, x+1, y+1)

#         dfs(root, 0, 0)

#         # Sort by column, then row, then value
#         nodes.sort(key=lambda x: (x[0], x[1], x[2]))

#         # Group by column
#         col_map = defaultdict(list)
#         for x, y, val in nodes:
#             col_map[x].append(val)
        
#         # Extract columns in increasing x order
#         return [col_map[x] for x in sorted(col_map)]

# ---- Second Solution: BFS
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []

        nodes = []
        q = deque([(root, 0, 0)])  # (node, x, y)
        while q:
            node, x, y = q.popleft()
            nodes.append((x, y, node.val))
            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        nodes.sort(key=lambda x: (x[0], x[1], x[2]))
        cols = defaultdict(list)
        for x, y, v in nodes:
            cols[x].append(v)
        return [cols[x] for x in sorted(cols)]
