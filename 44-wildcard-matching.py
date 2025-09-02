from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ---- First Solution
        """
        ? matches any single char; * matches any sequence (including empty).
        When you see *, remember its position (star) and the string index (match) where it started matching.
        On a later mismatch, "expand" that * to cover one more character: reset j = star+1, and advance i = match+1.
        Time Complexity: O(len(s) + len(p)); Space Complexity: O(1)
        """
        # i = j = 0                 # i over s, j over p
        # star = -1                 # last position of '*' in p (or -1 if none)
        # match = 0                 # position in s corresponding to that '*'

        # while i < len(s):
        #     # direct match or '?'
        #     if j < len(p) and (p[j] == s[i] or p[j] == '?'):
        #         i += 1
        #         j += 1
        #     # record a '*' and move pattern pointer
        #     elif j < len(p) and p[j] == '*':
        #         star = j
        #         match = i
        #         j += 1
        #     # mismatch: backtrack if we had a previous '*'
        #     elif star != -1:
        #         j = star + 1      # let '*' absorb one more char
        #         match += 1
        #         i = match
        #     else:
        #         return False

        # # consume trailing '*' in pattern
        # while j < len(p) and p[j] == '*':
        #     j += 1

        # return j == len(p)

        # ---- Second solution
        m, n = len(s), len(p)
        # dp[i][j] = does s[:i] match p[:j]?
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # An empty string can match a prefix of pattern only if that prefix is all '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                    # Current chars match (or '?' matches any one char):
                    # reduce to matching the previous prefixes
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # '*' can match:
                    #   - empty sequence  → dp[i][j-1]
                    #   - one more char   → dp[i-1][j]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                # else: dp[i][j] remains False (mismatch without '*')

        return dp[m][n]  # does full s match full pattern?