
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # First pass: find the candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Second pass: confirm the candidate if necessary (for generalized cases)
        # (not needed in this problem since we assume a majority element exists)
        return candidate


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         majority_elem = None
#         max_freq = 0
        
#         for num in nums:
#             count[num] = count.get(num, 0) + 1  # Efficient frequency counting
            
#             # Track the majority element during the loop
#             if count[num] > max_freq:
#                 majority_elem = num
#                 max_freq = count[num]
        
#         return majority_elem

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = dict()
#         for i, num in enumerate(nums):
#             count.update({num: 0})
#         for i, num in enumerate(nums):
#             count.update({num: count[num]+1})
#         max_freq = 0
#         for i, num in enumerate(nums):
#             if count[num] > max_freq:
#                 elem = num
#                 max_freq = max(max_freq, count[num])
#         return elem
