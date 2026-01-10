class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        dp[i][j] = minimum ASCII delete sum to make s1[i:] and s2[j:] equal
        """

        n, m = len(s1), len(s2)

        # DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: s1 exhausted → delete all remaining chars in s2
        for j in range(m - 1, -1, -1):
            dp[n][j] = dp[n][j + 1] + ord(s2[j])

        # Base case: s2 exhausted → delete all remaining chars in s1
        for i in range(n - 1, -1, -1):
            dp[i][m] = dp[i + 1][m] + ord(s1[i])

        # Fill DP table bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    # Characters match → no cost
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # Delete from either s1 or s2
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )

        return dp[0][0]
