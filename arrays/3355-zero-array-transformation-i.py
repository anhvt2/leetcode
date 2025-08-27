from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # We want to know if the given range-decrement operations (queries)
        # can reduce every nums[i] to 0 or below.
        #
        # Each query [l, r] represents *one unit* of decrement applied to every
        # index in the inclusive range [l, r]. If a position i is covered by K
        # queries, it receives K total decrements.
        #
        # Instead of applying each decrement to all elements in [l, r] (O(n * q)),
        # we build a "difference array" and later run a single prefix sum over it
        # to know, for each i, how many total decrements it gets.
        # Example: 
        #   queries = [[1, 3], [2, 4]]
        #   diffs = [0, 1, 1, 0, -1]
        #   prefix = [0, 1, 2, 2, 1]

        n = len(nums)
        diffs = [0] * n  # diffs[x] encodes "delta" changes to the running coverage

        # Build the difference array from queries
        for l, r in queries:
            # Mark: starting at l, coverage increases by +1
            diffs[l] += 1
            # Mark: just after r, coverage decreases by -1 (to stop the range)
            if r + 1 < n:
                diffs[r + 1] -= 1

        # Now accumulate the diffs to get, for each i, how many times it is covered
        # by the union of all queries (i.e., how many decrements it receives).
        prefix = 0  # running sum = current coverage count at index i
        for i in range(n):
            prefix += diffs[i]  # total decrements applied to position i
            # If the total decrements at i are fewer than nums[i],
            # we cannot reduce nums[i] down to 0 (we’d be short).
            if prefix < nums[i]:
                return False

        # Every index has enough coverage (decrements) to reach 0
        return True
