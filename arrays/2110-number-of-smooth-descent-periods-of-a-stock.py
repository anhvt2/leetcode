from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        """
        Algorithm:
        ----------
        A smooth descent period is a contiguous subarray where each adjacent
        price decreases by exactly 1.

        We iterate through the prices and track the length of the current
        smooth descent streak.

        - curr represents the length of the current valid descent ending at i.
        - At each index, curr is added to the answer because it contributes
          curr new descent periods ending at that index.

        If the descent condition breaks, reset curr to 1.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(prices)
        if n == 0:
            return 0

        ans = 1      # the first day alone is a valid period
        curr = 1     # current descent length

        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            ans += curr

        return ans
