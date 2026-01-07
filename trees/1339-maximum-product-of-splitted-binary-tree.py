# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm:
        1. Compute total sum of all nodes.
        2. DFS again to compute each subtree sum.
        3. For each subtree sum s, compute s * (total - s).
        4. Track the maximum product.
        """

        MOD = 10**9 + 7

        # Step 1: compute total tree sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)
        self.max_prod = 0

        # Step 2: compute subtree sums and evaluate products
        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Sum of the subtree rooted at this node
            subtree_sum = node.val + left_sum + right_sum

            # Product if we cut the edge above this subtree
            self.max_prod = max(
                self.max_prod,
                subtree_sum * (total - subtree_sum)
            )

            return subtree_sum

        dfs(root)
        return self.max_prod % MOD
