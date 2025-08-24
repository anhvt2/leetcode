from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # # ---- First solution: O(n) time, O(n) space
        # # Hash map
        # need = Counter()
        # ops = 0
        # for x in nums:
        #     y = k-x
        #     if need[y] > 0:
        #         ops += 1
        #         need[y] -= 1
        #     else:
        #         need[x] += 1
        # return ops

        # ---- Second solution: O(n log n) time, O(1) extra space
        # sort + two-pointers
        nums.sort()
        i, j = 0, len(nums) - 1
        ops = 0
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                ops += 1
                i += 1; j -= 1
            elif s < k:
                i += 1
            else: # s > k
                j -= 1
        return ops