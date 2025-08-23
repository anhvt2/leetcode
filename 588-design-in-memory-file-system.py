from typing import List

class FileSystem:
    class Node:
        __slots__ = ("children", "isFile", "content")
        def __init__(self):
            self.children = {}      # name -> Node
            self.isFile = False
            self.content = ""       # only used when isFile = True

    def __init__(self):
        self.root = self.Node()

    # /a/b/c -> ["a","b","c"]
    def _parts(self, path: str) -> List[str]:
        return [p for p in path.split('/') if p]

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.children.keys())
        node = self.root
        parts = self._parts(path)
        for name in parts:
            node = node.children[name]
        # file → return its own name; dir → sorted listing
        return [parts[-1]] if node.isFile else sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        node = self.root
        for name in self._parts(path):
            if name not in node.children:
                node.children[name] = self.Node()
            node = node.children[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = self._parts(filePath)
        node = self.root
        for name in parts[:-1]:                 # walk/create parent dirs
            if name not in node.children:
                node.children[name] = self.Node()
            node = node.children[name]
        fname = parts[-1]
        if fname not in node.children:
            node.children[fname] = self.Node()
            node.children[fname].isFile = True
        fnode = node.children[fname]
        # (LeetCode guarantees no conflict with existing directories)
        fnode.isFile = True
        fnode.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        for name in self._parts(filePath):
            node = node.children[name]
        return node.content
