class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(n) time complexity
        # O(n): space complexity
        h, n = len(haystack), len(needle)
        if n == 0:
            return 0
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1