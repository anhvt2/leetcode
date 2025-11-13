from math import gcd
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """Algorithm Steps
        1. Check if gcd(nums) is 1: If not, return -1.
        2. Count how many elements are already 1: If there are `count1` ones, you need `n - count1` operations to spread 1 to all others.
        3. If no 1 exists, find the shortest subarray with GCD 1:
        - For each i, compute GCD from i to j until GCD becomes 1.
        - Track the minimum length len of such subarrays.
        4. Total operations: If you found a subarray of length `len`, you need `len - 1` operations to create a `1`, then n - 1 more to spread it.
        """
        n = len(nums)
        overall_gcd = nums[0]
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)

        if overall_gcd > 1:
            return -1

        count1 = nums.count(1)
        if count1 > 0:
            return n - count1

        min_len = float('inf')
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i+1, n):
                curr_gcd = gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_len = min(min_len, j - i +1)
                    break
        return min_len - 1 + n - 1