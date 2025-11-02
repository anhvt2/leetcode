# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # Time: O(n), Space: O(h) - h is the height
        def dfs(node, current_sum):
            if not node:
                return 0


            # Build the number by multiplying previous sum by 10 and adding current digit
            current_sum = current_sum * 10 + node.val

            # If leaf node, return the complete number
            if not node.left and not node.right:
                return current_sum

            # Recursively sum left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)