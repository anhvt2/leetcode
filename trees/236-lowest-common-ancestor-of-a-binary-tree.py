# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            # Does this subtree started at `root` contain either p or q (or both)?
            if root is None:
                return None
            
            if root == p or root == q:
                return root
            # Idea: Start with left and go recursively until hit one of the node
            left = dfs(root.left, p, q)
            # Idea: Do the opposite
            right = dfs(root.right, p, q)

            # Start building up recursively and return LCA
            if left and right:
                return root
            elif not left:
                return right
            elif not right:
                return left
        return dfs(root, p, q)
