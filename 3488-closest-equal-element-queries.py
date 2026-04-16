class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Key idea:
        - For each value, collect all indices where it appears.
        - Since array is circular, for each index we want the closest
          same-value index either to the left or right (cyclically).

        Trick:
        - For each value group (sorted indices):
            For each index i:
                nearest candidates are:
                    previous occurrence
                    next occurrence
            BUT since circular, also consider wrap-around:
                first and last are neighbors

        Distance in circular array:
            dist(i, j) = min(|i-j|, n - |i-j|)

        Precompute for each index its answer.
        """

        from collections import defaultdict

        n = len(nums)

        pos = defaultdict(list)

        # group indices by value
        for i, x in enumerate(nums):
            pos[x].append(i)

        # answer for each index
        best = [-1] * n

        for arr in pos.values():
            if len(arr) == 1:
                continue

            m = len(arr)

            for i in range(m):
                cur = arr[i]

                # neighbors in circular list
                prev = arr[i - 1]               # wraps automatically
                nxt = arr[(i + 1) % m]

                # compute circular distances
                d1 = abs(cur - prev)
                d1 = min(d1, n - d1)

                d2 = abs(cur - nxt)
                d2 = min(d2, n - d2)

                best[cur] = min(d1, d2)

        # answer queries
        return [best[q] for q in queries]