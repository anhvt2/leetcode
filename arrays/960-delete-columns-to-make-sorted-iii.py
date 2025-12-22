from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Algorithm:
        ----------
        1. Treat each column as an element in a sequence.
        2. Find the longest sequence of columns such that for every row,
           characters are non-decreasing.
        3. This is a Longest Non-Decreasing Subsequence (LNDS) with constraints.
        4. Minimum deletions = total columns - LNDS length.

        Time Complexity: O(n^2 * m)
        Space Complexity: O(n)
        """

        m, n = len(strs), len(strs[0])

        # dp[j] = longest valid column sequence ending at column j
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                # Check if column i can come before column j
                valid = True
                for r in range(m):
                    if strs[r][i] > strs[r][j]:
                        valid = False
                        break

                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

        # Keep the longest valid subsequence
        return n - max(dp)
