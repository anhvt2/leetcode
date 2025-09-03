from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def helper(node: 'TreeNode') -> int:
            if not node:
                return 2
            if not node.left and not node.right:
                return 0

            left = helper(node.left)
            right = helper(node.right)

            if left == 0 or right == 0:
                self.max += 1
                return 1
            return 2 if left == 1 or right == 1 else 0

        return (1 if helper(root) < 1 else 0) + self.max
