"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        out = []

        def dfs(node: 'Node') -> None:
            out.append(str(node.val))
            out.append(str(len(node.children)))
            for ch in node.children:
                dfs(ch)

        dfs(root)
        return " ".join(out)        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        tokens = data.split()
        i = 0

        def build() -> 'Node':
            nonlocal i
            val = int(tokens[i]); i += 1
            k = int(tokens[i]);   i += 1
            node = Node(val, [])
            for _ in range(k):
                node.children.append(build())
            return node

        return build()        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))