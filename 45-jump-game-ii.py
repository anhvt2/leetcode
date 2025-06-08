
from typing import List
# from functools import lru_cache

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)

#         # @lru_cache(maxsize=None)
#         def dfs(i):
#             if i >= n - 1:
#                 return 0  # already at or beyond the last index
#             min_jumps = float('inf')
#             for j in range(1, nums[i] + 1):
#                 min_jumps = min(min_jumps, 1 + dfs(i + j))
#             return min_jumps

#         return dfs(0)

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest

        return jumps

