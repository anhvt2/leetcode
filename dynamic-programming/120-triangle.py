from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        # 1. Initialize dp as a copy of the last row.
        dp = triangle[-1][:]

        # 2. For each row walking backward, update the current element by adding (sum of its minimum children) and (current triangle element)
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update dp[j]:
                # The cost at (i, j) plus the cheaper of its two children
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        # 3. The top element is the answer
        return dp[0]
