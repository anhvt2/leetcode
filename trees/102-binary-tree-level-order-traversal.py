from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        q = deque([root])

        while q:
            level_count = len(q) # number of nodes at current level
            level_holder = []

            # Process all nodes at the current level
            for _ in range(level_count):
                node = q.popleft() # Pop the front node from the queue
                level_holder.append(node.val)
                # Enqueue left and right children if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(level_holder)
        return result