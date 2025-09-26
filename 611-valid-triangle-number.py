from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        # k is the index of the largest side in the triangle
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                # other two constraints are naturally satisfied by sort(), so only check the last constraint
                if nums[i] + nums[j] > nums[k]:
                    count += j - i # if the smallest i satistifies, then every element between i and j also satisfy
                    j -= 1
                else:
                    i += 1

        return count
