# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node) -> [int, int]:
            """
            Returns (sum_subtree, size_subtree) for 'node'
            Also increments self.count if node.val equals sum_subtree // size_subtree
            """
            if not node:
                return 0, 0

            # Post-order: compute children first
            lsum, lcount = dfs(node.left)
            rsum, rcount = dfs(node.right)

            total_sum = lsum + rsum + node.val
            total_count = lcount + rcount + 1

            if node.val == total_sum // total_count:
                self.count += 1

            return total_sum, total_count

        dfs(root)
        return self.count