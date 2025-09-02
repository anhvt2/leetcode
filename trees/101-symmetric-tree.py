from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # ---- First Solution
        # if not root:
        #     return True
        
        # def is_mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        #     if not a and not b:
        #         return True
        #     if not a or not b or a.val != b.val:
        #         return False
        #     # outside with outside, inside with inside
        #     return is_mirror(a.left, b.right) and is_mirror(a.right, b.left)
        
        # return is_mirror(root.left, root.right)
        # ---- Second Solution
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            a, b = q.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            q.append((a.left, b.right))
            q.append((a.right, b.left))
        return True