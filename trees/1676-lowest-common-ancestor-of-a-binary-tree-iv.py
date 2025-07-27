# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # use a recursive postorder traversal
        # recurse on left or right
        # if both sides return non-null, then current node is the LCA
        # if only one side returns non-null, propagate it up
        node_set = set(nodes) # for O(1) lookup

        def dfs(node):
            if not node:
                return None
            if node in node_set:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            return left or right
        
        return dfs(root)
