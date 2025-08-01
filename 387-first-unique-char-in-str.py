class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1
