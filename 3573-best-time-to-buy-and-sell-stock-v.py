from typing import List
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # Can't do more than floor(n/2) non-overlapping 2-day transactions
        k = min(k, n // 2)

        # dp_prev[i] = max profit using <= (t−1) transactions up to day i
        # dp_curr[i] = max profit using <= t transactions up to day i
        dp_prev = [0] * n
        dp_curr = [0] * n

        for t in range(1, k + 1):
            # bestLong = max_{a< i}( dp_prev[a−1] − prices[a] )
            # bestShort = max_{a< i}( dp_prev[a−1] + prices[a] )
            # initialize both for a=0 (dp_prev[−1] is 0)
            bestLong = -prices[0]
            bestShort =  prices[0]
            dp_curr[0] = 0

            for i in range(1, n):
                # 1) skip day i -> dp_curr[i−1]
                # 2) end a "long" transaction at i -> bestLong + prices[i]
                # 3) end a "short" transaction at i -> bestShort − prices[i]
                dp_curr[i] = max(
                    dp_curr[i-1],
                    bestLong + prices[i],
                    bestShort - prices[i]
                )

                # Now allow a=i to seed future transactions:
                prev = dp_prev[i-1]
                bestLong  = max(bestLong, prev - prices[i])
                bestShort = max(bestShort, prev + prices[i])

            # roll forward
            dp_prev, dp_curr = dp_curr, dp_prev

        return dp_prev[-1]
