# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # ---- First Solution
        def dfs(root: TreeNode, s: str):
            if not root.left and not root.right:
                res.append(s)
            if root.left:
                dfs(root.left, s + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, s + '->' + str(root.right.val))
        res = []
        dfs(root, str(root.val))
        return res
        
        # ---- Second Solution
        # if not root:
        #     return []

        # paths = []
        # def dfs(node: 'TreeNode', cur: List[str]) -> None:
        #     # Append current node value to the path
        #     cur.append(str(node.val))

        #     # If it's a leaf, join the path and store it
        #     if not node.left and not node.right:
        #         paths.append("->".join(cur))
        #     else:
        #         # Recurse to children
        #         if node.left:
        #             dfs(node.left, cur)
        #         if node.right:
        #             dfs(node.right, cur)
        #     # Backtrack
        #     cur.pop()

        # dfs(root, [])
        # return paths
