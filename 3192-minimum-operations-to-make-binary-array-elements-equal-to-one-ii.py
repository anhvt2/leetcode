from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        target = 1  # what the current bit should be after prior flips
        for x in nums:
            if x != target:
                ops += 1
                target ^= 1  # future bits are toggled by this suffix flip
        return ops
