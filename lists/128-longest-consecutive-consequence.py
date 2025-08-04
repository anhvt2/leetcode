# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = sorted(list(set(nums)))
#         res = []
#         tmp = []
#         for i, num in enumerate(nums):
#             if not tmp:
#                 tmp.append(num)
#             else:
#                 if num == tmp[-1] + 1:
#                     tmp.append(num)
#                 else:
#                     res.append(tmp)
#                     tmp = [num] # reset but don't drop the current num
#         res.append(tmp)
#         return max([len(chunk) for chunk in res])