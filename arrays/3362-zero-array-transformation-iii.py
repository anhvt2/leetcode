from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # bucket queries by start l
        byL = [[] for _ in range(n)]
        for l, r in queries:
            if 0 <= l < n:
                byL[l].append(r)

        # max-heap of r for all queries with l <= i (store as negative for Python heap)
        pool = []

        # difference array to accumulate coverage contributed by kept queries
        add = [0] * (n + 1)
        cover = 0     # running coverage at i = sum(add[:i+1])
        kept = 0      # how many queries we decided to keep

        for i in range(n):
            # add newly available queries that start at i
            for r in byL[i]:
                heapq.heappush(pool, -r)

            # update current coverage from previous picks
            cover += add[i]

            # ensure enough decrements at i
            need = nums[i] - cover
            while need > 0:
                if not pool:
                    return -1
                r = -heapq.heappop(pool)
                if r < i:
                    # best available interval doesn't even cover i -> impossible
                    return -1

                # pick this query:
                kept += 1
                cover += 1
                need -= 1

                # this query contributes +1 to all j in [i, r]
                # encode via difference array so future indices get it "for free"
                if r + 1 <= n - 1:
                    add[r + 1] -= 1

        # maximum removable = total - kept
        return len(queries) - kept
