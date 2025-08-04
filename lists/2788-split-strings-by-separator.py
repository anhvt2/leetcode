class Solution:
    def splitWordsBySeparator(self, 
                             words: List[str], 
                             separator: str) -> List[str]:
        res = []
        for i, word in enumerate(words):
            parts = word.split(separator)
            res += [part for part in parts if part]
        return res