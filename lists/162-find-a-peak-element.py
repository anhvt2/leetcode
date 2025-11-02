# Time complexity: O(log n)
# Space complexity: O(1)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # if slope is rising, go right
            if nums[mid] < nums[mid+1]:
                left = mid + 1 
            else:
                # slope is falling, go left
                right = mid
        # peak is where left == right
        return left

# Time complexity: O(n)
# Space complexity: O(1)

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return 0
#         elif len(nums) == 2:
#             return 0 if nums[0] > nums[1] else 1
#         else:
#             for i in range(1, len(nums) - 1):
#                 if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
#                     return i
#             if nums[0] > nums[1]:
#                 return 0
#             elif nums[-1] > nums[-2]:
#                 return len(nums)-1