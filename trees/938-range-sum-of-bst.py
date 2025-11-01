# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        # If current node is less than low, only search right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If current node is greater than high, only search left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # Current node is in range, add it and search both subtree
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low,high)