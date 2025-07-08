class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False  # Can't reach this point
            farthest = max(farthest, i + nums[i])
        return True
