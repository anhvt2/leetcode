# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return -1
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter at this node (left_depth + right_depth + 2)
            self.diameter = max(self.diameter, left_depth + right_depth + 2)
            
            # Return the depth of this node (max depth of left or right subtree + 1)
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
