from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Main entry point:
        1) Extract sorted values from BST
        2) Build a balanced BST from those values
        """

        # Step 1: inorder traversal to get sorted values
        nums = []
        self.inorder(root, nums)

        # Step 2: build balanced BST from sorted array
        return self.build(nums, 0, len(nums) - 1)

    def inorder(self, node: TreeNode, nums: List): -> List[int]
        """
        Inorder traversal of BST:
        left -> node -> right
        Produces list of values from tree nodes in sorted order
        """
        if not node:
            return
        # Binary tree is already sorted, so append in order to keep it sortde
        self.inorder(node.left, nums)
        nums.append(node.val)
        self.inorder(node.right, nums)

    def build(self, nums: List, left: int, right: int) -> TreeNode:
        """
        Build a height-balanced BST from sorted array nums[left:right+1]
        """
        if left > right:
            return None

        # Choose middle element to ensure balance
        mid = (left + right) // 2
        root = TreeNode(nums[mid])

        # Recursively build left and right subtrees
        root.left = self.build(nums, left, mid - 1)
        root.right = self.build(nums, mid + 1, right)

        return root
