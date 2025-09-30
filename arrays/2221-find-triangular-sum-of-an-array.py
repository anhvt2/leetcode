from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        # Work in-place: after each pass, last element becomes obsolete
        for end in range(n - 1, 0, -1):
            for i in range(end):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]
