from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Algorithm:
        ----------
        For each column:
          - Check if characters are non-decreasing from top to bottom.
          - If any violation exists, delete that column.

        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """

        rows = len(strs)
        cols = len(strs[0])
        deletions = 0

        for c in range(cols):
            for r in range(rows - 1):
                # If column c is not sorted
                if strs[r][c] > strs[r + 1][c]:
                    deletions += 1
                    break  # no need to check further rows

        return deletions
