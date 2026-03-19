# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # base case
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            
            # number of valid paths ending here
            res = prefix_count[curr_sum - targetSum]
            
            # add current prefix sum
            prefix_count[curr_sum] += 1
            
            # explore
            res += dfs(node.left, curr_sum)
            res += dfs(node.right, curr_sum)
            
            # backtrack
            prefix_count[curr_sum] -= 1
            
            return res
        
        return dfs(root, 0)