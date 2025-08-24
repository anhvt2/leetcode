class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # Pay particular attention to unique requirement
        # O(n) time; O(1) space
        # Track the current length of the wraparound run and a `dp[26]` where `dp[i]` is the longest wraparound length of substrings ending with letter i. Answer: sum(dp)
        # For a fixed ending letter ch, the number of distinct substrings ending at ch equals the length of the longest valid run ending at ch. Shorter ones are all suffixes of that run and hence already counted.
        if not s:
            return 0
        dp = [0] * 26       # dp[c]: max length of wrap run ending at char ch
        curr = 0            # current consecutive length in wraparound

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i-1]) + 26) % 26 == 1:
                curr += 1
            else:
                curr = 1
            idx = ord(ch) - ord('a')
            dp[idx] = max(dp[idx], curr)
        return sum(dp)
    