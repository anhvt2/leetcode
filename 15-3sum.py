# # Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# # Notice that the solution set must not contain duplicate triplets.

from typing import List, Optional
from collections import deque, Counter
import bisect

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triple_lists = [] # deque()
#         n = len(nums)
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 for k in range(j+1,n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         tmp = sorted([nums[i], nums[j], nums[k]])
#                         if tmp not in triple_lists:
#                             triple_lists.append(tmp)

#         return triple_lists

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         counts = Counter(nums)
#         zero_count = counts.pop(0,0)
#         result = [[0, 0, 0]] if zero_count >= 3 else []  # The only triplet with all duplicates
        
#         if len(counts) < 2:
#             return result
        
#         unique = list(counts)
    
#         # Find all remaining triplets that include 0
#         if zero_count:
#             for num in unique:
#                 if num > 0:
#                     break
#                 if -num in counts:
#                     result.append([num, 0, -num])

#         # Find all triplets with two duplicates
#         for num in unique:
#             if num % 2:
#                 continue
#             candidate = -num // 2
#             if counts[candidate] >= 2:
#                 result.append([num, candidate, candidate])
    
#         # Find all remaining triplets with no duplicates
#         start = bisect.bisect_right(unique, max(-unique[-1] // 2, unique[0]))
#         #return start
#         stop = bisect.bisect_left(unique, min(-(unique[0] // 2), unique[-1]))
#         for i in range(start, stop):
#             num = unique[i]
#             j = bisect.bisect_right(unique, -num * 2) if num < 0 else i + 1
#             k = bisect.bisect_right(unique, -unique[0] - num)
#             for right in unique[j:k]:
#                 left = -num - right
#                 if left in counts:
#                     result.append([left, num, right])
    
#         return result

nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
sol = Solution()
res = sol.threeSum(nums)
print(res)
