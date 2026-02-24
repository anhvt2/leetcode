# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            
            # shift left (multiply by 2) and add current bit
            current = (current << 1) | node.val
            
            # if leaf → return computed number
            if not node.left and not node.right:
                return current
            
            # sum from left and right subtrees
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)