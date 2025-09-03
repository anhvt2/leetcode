from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf') # 'best' tracks the best of any path seen so far, including one that bends at node to take both children
        # Time Complexity: O(N) - visit each node once
        # Space Complexity: O(H) - recursion stack (H = tree height)
        def gain(node: Optional[TreeNode]) -> int:
            # gain(node) returns the best sum of a path that starts at node and goes up through exactly one child (or none).
            nonlocal best
            if not node:
                return 0
        
            # Max gain from children; drop negatives as they reduce the sum
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)

            # Path using node as the peak: left + node + right
            best = max(best, node.val + left_gain + right_gain)
            
            # Return max one-side gain to parent
            return node.val + max(left_gain, right_gain)
        
        gain(root)
        return best
