class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        """
        Key idea:
        - We need 3 indices i < j < k with nums[i] == nums[j] == nums[k]
        - Distance simplifies:

            |i-j| + |j-k| + |k-i|
          = (j-i) + (k-j) + (k-i)
          = 2 * (k - i)

        So for any valid triple, distance depends ONLY on outermost indices.

        Therefore:
        - For each value, collect all indices where it appears.
        - Try all triples of occurrences and minimize:
              2 * (max_index - min_index)

        But we must ensure at least 3 occurrences.
        """

        from collections import defaultdict

        pos = defaultdict(list)

        # group indices by value
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = float('inf')

        # check each value group
        for arr in pos.values():
            if len(arr) < 3:
                continue

            # brute all triples (n ≤ 100 so safe)
            m = len(arr)
            for i in range(m):
                for j in range(i + 1, m):
                    for k in range(j + 1, m):
                        # compute distance
                        dist = 2 * (arr[k] - arr[i])
                        ans = min(ans, dist)

        return -1 if ans == float('inf') else ans