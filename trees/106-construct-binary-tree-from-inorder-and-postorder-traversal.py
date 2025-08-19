# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, 
                    inorder: List[int], 
                    postorder: List[int]
                ) -> Optional[TreeNode]:
        # inorder: left -> root -> right
        # postorder: left -> right -> root
        if not inorder or not postorder or len(inorder) != len(postorder):
            return None
        
        # Map each value in inorder to its index for O(1) lookup
        idx_map = {val: i for i, val in enumerate(inorder)}

        # Recursive helper: build tree from inorder[l..r], consuming postorder from the end
        def helper(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            
            # (1) The current root value is the last in postorder
            root_val = postorder.pop()
            root = TreeNode(val=root_val)
            # (2) Split inorder array around root_val
            mid = idx_map[root_val]
            # (3) Build right subtree first (because postorder pops root last, so just before that are the nodes of the right subtree)
            root.right = helper(mid+1, r)
            # (4) Then build the left subtree
            root.left = helper(l, mid-1)
            return root
        
        # Entire inorder range is [0..n-1]
        return helper(0, len(inorder)-1)
        