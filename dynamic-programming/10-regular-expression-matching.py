class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dynamic programming: bottom-up
        # dp[i][j] means: does s[0:i] match p[0:j]
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        # Pre-fill for patterns like a*, a*b, etc. that can match empty string
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # Zero occurance
                    dp[i][j] = dp[i][j-2]
                    # At least one
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] |= dp[i-1][j] # dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[m][n]