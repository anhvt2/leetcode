from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # take: max if we rob this node (then we can't rob its children)
        # skip: max if we skip this node (then we can choose best from each child)
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if not node:
                return 0, 0 # (take, skip) for null
            lt, ls = dfs(node.left) # left take, left skip
            rt, rs = dfs(node.right) # right take, right skip
            take = node.val + ls + rs
            skip = max(lt, ls) + max(rt, rs)
            return take, skip
        
        return max(dfs(root))