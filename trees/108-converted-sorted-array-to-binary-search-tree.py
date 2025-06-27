# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Step:
#     Choose the middle element of the current subarray as the root.
#     Recursively build the left subtree using the subarray to the left of mid.
#     Recursively build the right subtree using the subarray to the right of mid.
# This guarantees balance because the left and right subtrees will have roughly the same number of nodes.

# Explanation
#     The helper function build(left, right) builds the BST from nums[left:right+1].
#     At each step:
#         It picks the middle value as the current node.
#         Recursively builds the left and right children.

# O(n) time complexity
# A binary search tree always keeps smaller values to the left, greater values to the right, at every node - recursively.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)
            return node

        return build(0, len(nums) - 1)
