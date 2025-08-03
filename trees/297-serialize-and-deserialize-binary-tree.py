# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        1. Traverse tree in preorder (root -> left -> right)
        2. Append each non-None node value to a list
        3. For None children, append None
        4. Joint list by commas into a single string
        """
        vals = []
        def dfs(node: TreeNode):
            if not node:
                vals.append('None')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(vals)
        

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        1. Split the string on commas to recover token list
        2. Use a queue (or index pointer) to consume token in order
        3. Rebuild tree recursively:
            a. If the next token = None, consume it and return None
            b. If not None, then create a TreeNode(int(token)), then recursively build its left and right subtrees
        """
        tokens = deque(data.split(','))

        def build() -> TreeNode:
            if not tokens:
                return None
            val = tokens.popleft()
            if val == 'None':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))