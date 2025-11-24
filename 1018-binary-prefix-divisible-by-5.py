from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        mod = 0
        for b in nums:
            mod = (mod * 2 + b) % 5
            result.append(mod == 0)
        return result