from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False

        diff1 = nums[1] - nums[0]
        if diff1 <= 0:
            return False  # first segment must increase

        phase = 0  # 0=incr, 1=decr, 2=incr
        for i in range(1, len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff == 0:
                return False
            if phase == 0:
                if diff > 0:
                    continue
                else:
                    phase = 1  # start decreasing
            elif phase == 1:
                if diff < 0:
                    continue
                else:
                    phase = 2  # start second increasing
            else:
                if diff > 0:
                    continue
                else:
                    return False

        return phase == 2
