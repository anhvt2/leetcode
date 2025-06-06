from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {} # number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
            # print(num_to_index)
        return [] # return [-1, -1]

nums = [3,2,4]
target = 6
sol = Solution()
result = sol.twoSum(nums, target)
print(result)
