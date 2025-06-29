from collections import deque
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        indices = [index for num, index in sorted_nums]
        indices.sort()
        return [nums[i] for i in indices]
