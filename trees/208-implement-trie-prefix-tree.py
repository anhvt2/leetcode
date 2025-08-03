
class Trie:
    def __init__(self):
        # The root is just an empty dict
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            # setdefault will return the child dict if it exists
            # or insert a new empty dict and return that
            node = node.setdefault(ch, {})
        # mark the end of a word with a special key
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        # only true if we have explicitly marked the end of a word
        return node.get('#', False)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
