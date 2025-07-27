# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found_p = False
        self.found_q = False
        
        def dfs(node):
            if not node:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p:
                self.found_p = True
                return node

            if node == q:
                self.found_q = True
                return node

            if left and right:
                return node
            return left or right
        
        lca = dfs(root)
        if self.found_p and self.found_q:
            return lca
        return None

