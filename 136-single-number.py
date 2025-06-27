class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result
        


# from typing import List
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         my_dict = dict()
#         for i in range(len(nums)):
#             my_dict.update({nums[i]: 0})
#         for i in range(len(nums)):
#             my_dict[nums[i]] += 1
#             if my_dict[nums[i]] > 1:
#                 my_dict.pop(nums[i])
#         return list(my_dict)[0]

