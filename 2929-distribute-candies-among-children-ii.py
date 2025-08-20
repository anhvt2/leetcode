import numpy as np

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Create an array of all possible values of 'a' from 0 to limit (inclusive)
        a = np.arange(limit + 1)  # shape: (limit+1,)

        # For each value of 'a', compute the valid range of 'b' such that:
        # - 0 <= b <= limit
        # - 0 <= c = n - a - b <= limit
        # So:
        #    b_min = max(0, n - limit - a)
        #    b_max = min(limit, n - a)
        # Number of valid b's is: b_max - b_min + 1
        diff = np.minimum(limit, n - a) - np.maximum(0, n - limit - a) + 1

        # Remove negative values (invalid cases where range is empty)
        diff = np.maximum(0, diff)

        # Sum over all valid (a, b, c) triplets
        return np.sum(diff)

