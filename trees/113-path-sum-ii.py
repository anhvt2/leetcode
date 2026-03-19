# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            
            # include current node
            path.append(node.val)
            remaining -= node.val
            
            # check leaf
            if not node.left and not node.right and remaining == 0:
                res.append(path[:])  # copy
            
            # recurse
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)
            
            # backtrack
            path.pop()
        
        dfs(root, targetSum, [])
        return res        