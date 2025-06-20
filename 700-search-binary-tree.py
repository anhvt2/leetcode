# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == val:
            return root
        else:
            # Search in the left or right subtree, return the result of the search
            left_search = self.searchBST(root.left, val)
            if left_search:
                return left_search
            return self.searchBST(root.right, val)
