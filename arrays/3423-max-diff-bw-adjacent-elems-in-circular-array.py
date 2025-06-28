# Given a circular array nums, find the maximum absolute difference between adjacent elements.
# Note: In a circular array, the first and last elements are adjacent.
# class Solution:
#     def maxAdjacentDistance(self, nums: List[int]) -> int:
#         diff = abs(nums[-1] - nums[0])
#         for i in range(len(nums) - 1):
#             diff = max(diff, abs(nums[i+1] - nums[i]))
#         return diff

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = 0
        n = len(nums)
        for i in range(n):
            diff = max(diff, abs(nums[(i+1)%n] - nums[i]))
        return diff
