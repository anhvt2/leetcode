class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_diff = float('+inf')
        tracked_idx = -1
        for i in range(len(nums)):
            if nums[i] == target and abs(i-start) < min_diff:
                tracked_idx = i
                min_diff = abs(i-start)
        return abs(tracked_idx - start)
