from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Dynamic Programming

        dp[i][j] = maximum dot product using subsequences
                   from nums1[i:] and nums2[j:]
        """

        n, m = len(nums1), len(nums2)

        # Initialize DP table with very negative values
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        # Base case:
        # When either array is exhausted, dot product is invalid
        # unless something was already taken
        for i in range(n + 1):
            dp[i][m] = float('-inf')
        for j in range(m + 1):
            dp[n][j] = float('-inf')

        # Fill DP table bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                # Option 1: Take current pair
                product = nums1[i] * nums2[j]
                take = product + max(0, dp[i + 1][j + 1])

                # Option 2: Skip nums1[i]
                skip1 = dp[i + 1][j]

                # Option 3: Skip nums2[j]
                skip2 = dp[i][j + 1]

                dp[i][j] = max(take, skip1, skip2)

        return dp[0][0]
