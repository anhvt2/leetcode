# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         tmp = []
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 tmp.append(i)
#         if len(tmp) > 0:
#             return [min(tmp), max(tmp)]
#         else:
#             return [-1, -1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search for left in O(log n)
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target :
                left = mid + 1
            else:
                right = mid - 1
        
        tmp = []
        tmp.append(left)
        # search for left in O(log n)
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        tmp.append(right)
        return tmp if len(tmp) > 1 and tmp[0] <= tmp[1] else [-1, -1]
    