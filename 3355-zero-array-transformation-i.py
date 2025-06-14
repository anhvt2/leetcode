# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

# For each queries[i]:
#     Select a subset of indices within the range [li, ri] in nums.
#     Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.
# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

# Key Insight
# You can choose any subset of indices in each range.
# So, for each index j, the maximum number of decrements possible at that index is the number of queries that cover index j.
# To be able to make every value in nums zero, for every index j, the number of queries covering it must be at least as large as nums[j].
# If for any j, nums[j] > (number of queries covering j), it is impossible.


from typing import List, Optional

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        # Build difference array
        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        # Prefix sum to get cover count for each index
        cover = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            cover[i] = curr
        # Check if every number can be zeroed out
        for i in range(n):
            if nums[i] > cover[i]:
                return False
        return True
