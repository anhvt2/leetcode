from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        Algorithm:
        ----------
        1. Sort happiness values in descending order.
        2. Select the top k children.
        3. For the t-th selected child, contribute:
              max(happiness[t] - t, 0)
        4. Sum the contributions.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """

        # Sort happiness values from largest to smallest
        happiness.sort(reverse=True)

        total = 0

        for t in range(k):
            # Each subsequent selection reduces happiness by t
            contribution = max(happiness[t] - t, 0)
            total += contribution

        return total
