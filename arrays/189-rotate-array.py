# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

from typing import List, Optional
from collections import deque

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         queue = deque(nums)
#         for i in range(k):
#             last = queue.pop()
#             queue.appendleft(last)
#         # Write back to nums
#         for i in range(n):
#             nums[i] = queue[i]
#         # return queue

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k > n
        # Use list slicing
        nums[:] = nums[-k:] + nums[:-k]


sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums, k))
