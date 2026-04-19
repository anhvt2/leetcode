class Solution:
    def minimumScore(self, nums):
        """
        Key idea:
        - We need 3 indices i, j, k with same value.
        - Distance simplifies to:
              |i-j| + |j-k| + |k-i| = 2 * (k - i)  if i < j < k

        So the problem becomes:
        - For each value, find 3 occurrences minimizing (max - min)
        - We only need to consider sliding windows of size 3 over indices.

        Optimization:
        - We do NOT need O(m^3).
        - For each value, only check consecutive triples in its index list.
          (Because using non-consecutive middle points never improves min span)
        """

        from collections import defaultdict

        pos = defaultdict(list)

        # collect indices for each value
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        # process each value group
        for arr in pos.values():
            if len(arr) < 3:
                continue

            # sliding window of size 3 on sorted indices
            for i in range(len(arr) - 2):
                # best triple is consecutive occurrences
                # i, i+1, i+2 minimizes (max - min)
                dist = 2 * (arr[i + 2] - arr[i])
                ans = min(ans, dist)

        return -1 if ans == float('inf') else ans