# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Start with the root node in the queue
        
        while queue:
            level_sum = 0
            level_count = len(queue)  # Number of nodes at the current level
            
            # Process all nodes at the current level
            for _ in range(level_count):
                node = queue.popleft()  # Pop the front node from the queue
                level_sum += node.val  # Add its value to the level sum
                
                # Enqueue left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Compute the average for this level
            result.append(level_sum / level_count)
        
        return result
