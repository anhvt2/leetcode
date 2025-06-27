class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:    # if the tree is empty, return False
            return False

        if not root.left and not root.right:
            return root.val == targetSum
        
        # recursively check for left or right subtree with reduced targetSum
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )

# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         # Base case: if the root is None, no path exists
#         if not root:
#             return False
        
#         # Subtract the current node's value from the target sum
#         targetSum -= root.val
        
#         # If we reached a leaf node (both left and right children are None)
#         if not root.left and not root.right:
#             return targetSum == 0  # If the target sum becomes 0, return True
        
#         # Recursively check both left and right subtrees
#         return (self.hasPathSum(root.left, targetSum) or 
#                 self.hasPathSum(root.right, targetSum))
