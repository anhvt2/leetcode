class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        share = 0  # number of people who can share the secret today

        for day in range(2, n + 1):
            # People who become able to share today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            # People who forget today (no longer share starting today)
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD

            dp[day] = share % MOD

        # Sum of those who still remember on day n
        start = max(1, n - forget + 1)
        return sum(dp[start : n + 1]) % MOD
