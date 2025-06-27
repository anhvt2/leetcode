class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        else:
            incr = nums[-1] - nums[0]
            if incr > 0:
                for i in range(len(nums)-1): # monotonically increasing
                    if nums[i] > nums[i+1]:
                        return False
                return True
            else:
                for i in range(len(nums)-1): # monotonically decreasing
                    if nums[i] < nums[i+1]:
                        return False
                return True
