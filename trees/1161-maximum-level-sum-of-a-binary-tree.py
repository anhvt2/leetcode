# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm:
        - Perform BFS (level-order traversal).
        - Compute the sum of values at each level.
        - Track the maximum sum and the corresponding level.
        - Return the smallest level index with the maximum sum.
        """

        # Queue for BFS, initialized with the root node
        queue = deque([root])

        # Level index starts at 1 (problem is 1-indexed)
        level = 1

        # Track the maximum sum and its level
        max_sum = float('-inf')
        max_level = 1

        # Standard BFS loop
        while queue:
            level_sum = 0
            size = len(queue)  # number of nodes at the current level

            # Process all nodes at the current level
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max sum and level if this level is better
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            # Move to next level
            level += 1

        return max_level