from typing import List
import math

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # ans starts at negative infinity to allow all-negative arrays
        ans = -10**30
        prefix = 0
        # minPrefix[r] = minimum prefix sum s_j seen so far where j % k == r
        INF = 10**30
        minPrefix = [INF] * k
        # include the empty prefix at index j = -1 whose remainder is (-1) % k == k-1
        minPrefix[( -1) % k] = 0

        for i, x in enumerate(nums):
            prefix += x
            r = i % k
            # best subarray ending at i with length divisible by k:
            # prefix - minimum prior prefix with same remainder
            if minPrefix[r] != INF:
                candidate = prefix - minPrefix[r]
                if candidate > ans:
                    ans = candidate
            # update the minimum prefix for this remainder class
            if prefix < minPrefix[r]:
                minPrefix[r] = prefix

        return ans
