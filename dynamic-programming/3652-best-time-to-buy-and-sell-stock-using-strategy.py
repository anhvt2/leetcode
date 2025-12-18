from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        """
        Algorithm:
        ----------
        1. Compute the base profit = sum(strategy[i] * prices[i]).
        2. Use prefix sums to efficiently compute:
           - Original contribution of any k-length window.
           - Modified contribution (sum of prices in the last k/2 positions).
        3. Slide a window of length k and compute the gain from modification.
        4. Add the maximum gain (if positive) to the base profit.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        n = len(prices)

        # Step 1: Base profit
        base_profit = sum(s * p for s, p in zip(strategy, prices))

        # Step 2: Prefix sums
        price_prefix = [0] * (n + 1)
        contrib_prefix = [0] * (n + 1)

        for i in range(n):
            price_prefix[i + 1] = price_prefix[i] + prices[i]
            contrib_prefix[i + 1] = contrib_prefix[i] + strategy[i] * prices[i]

        max_gain = 0
        half = k // 2

        # Step 3: Sliding window
        for l in range(n - k + 1):
            r = l + k

            # Original contribution in [l, r)
            original = contrib_prefix[r] - contrib_prefix[l]

            # Modified contribution:
            # first k/2 → 0
            # last k/2 → sell (sum of prices)
            modified = price_prefix[r] - price_prefix[l + half]

            gain = modified - original
            max_gain = max(max_gain, gain)

        # Step 4: Result
        return base_profit + max_gain
