from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0
        for i in range(n - 2):
            if nums[i] == 0:
                # flip i, i+1, i+2
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1
        # after fixing up to n-3, the last two must already be 1
        return -1 if nums[n - 1] == 0 or nums[n - 2] == 0 else ops
