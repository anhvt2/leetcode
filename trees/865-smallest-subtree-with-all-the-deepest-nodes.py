# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Returns the smallest subtree containing all deepest nodes.
        Uses post-order DFS.
        """

        def dfs(node):
            """
            Returns:
            - depth: maximum depth from this node downward
            - subtree_root: root of the subtree containing all deepest nodes
            """
            if not node:
                return 0, None

            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            # If left subtree is deeper, propagate it upward
            if left_depth > right_depth:
                return left_depth + 1, left_subtree

            # If right subtree is deeper, propagate it upward
            if right_depth > left_depth:
                return right_depth + 1, right_subtree

            # If depths are equal, current node is the LCA
            return left_depth + 1, node

        # The subtree root is the second value of the result
        return dfs(root)[1]
