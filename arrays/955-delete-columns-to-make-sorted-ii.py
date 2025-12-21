from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Algorithm:
        ----------
        Greedy column-by-column comparison.

        Maintain `sorted[i]`:
          - True means strs[i] < strs[i+1] is already fixed by previous columns.

        For each column:
          - If any unresolved pair violates order, delete column.
          - Otherwise, update resolved pairs.

        Time Complexity: O(m * n)
        Space Complexity: O(m)
        """

        m = len(strs)
        n = len(strs[0])
        deletions = 0

        # sorted[i] == True means strs[i] < strs[i+1] already confirmed
        sorted_pair = [False] * (m - 1)

        for col in range(n):
            # Check if this column breaks lexicographic order
            should_delete = False
            for i in range(m - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    should_delete = True
                    break

            if should_delete:
                deletions += 1
                continue

            # Update sorted pairs
            for i in range(m - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

            # Optimization: all pairs resolved
            if all(sorted_pair):
                break

        return deletions
