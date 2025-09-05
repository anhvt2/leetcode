from functools import reduce
from operator import mul

MOD = 1_000_000_007

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        # All combinations if we only require length >= number of runs
        total = 1
        for g in groups:
            total = (total * g) % MOD

        m = len(groups)
        if k <= m:
            return total

        # dp[j] = number of ways to make intended length exactly j using processed groups
        dp = [0] * k
        dp[0] = 1

        # For each run of length g, you can "shorten" intended length by choosing
        # an offset in [0 .. g-1]; sliding window sums bound choices by g.
        for i, g in enumerate(groups):
            new = [0] * k
            window = 0
            for j in range(i, k):           # minimal length after i runs is i
                new[j] = (new[j] + window) % MOD
                window = (window + dp[j]) % MOD
                if j >= g:
                    window = (window - dp[j - g]) % MOD
            dp = new

        invalid_lt_k = sum(dp) % MOD        # counts lengths 0..k-1
        return (total - invalid_lt_k) % MOD
