from typing import List
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] = max number of strings using at most i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            # update backwards so each string used at most once
            for i in range(m, cnt0 - 1, -1):
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - cnt0][j - cnt1] + 1)
        
        return dp[m][n]
