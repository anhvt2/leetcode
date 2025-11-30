from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Return the minimum number of single-unit decrement operations
        (each operation replaces nums[i] with nums[i] - 1) required
        so that the sum of the array becomes divisible by k.

        The key observation:
            - Each operation decreases the total sum by exactly 1.
            - If S = sum(nums), and S % k = r, then decreasing S by r
              yields S - r which is divisible by k.
            - It's impossible to do fewer than r operations because operations
              only decrease the sum, and the next smaller multiple of k is
              (S - r) - k which requires k + r decreases.

        Therefore the answer is r = S % k.
        """
        # Defensive check: k must be >= 1 for modulo to make sense.
        # (By problem statement k is positive; this check is for clarity.)
        if k <= 0:
            raise ValueError("k must be a positive integer")

        # Compute total sum of the array. This is O(n).
        total_sum = sum(nums)

        # The remainder when total_sum is divided by k is exactly the minimum
        # number of single-step decrements needed.
        # Example: if total_sum = q*k + r, then total_sum - r = q*k is divisible.
        return total_sum % k
