class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        s = 0
        for i in range(0,n,2):
            s += nums[i]
        return s
