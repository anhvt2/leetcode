class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Cost = nums[0] + two smallest values in nums[1:]
        # nums[0] is always the start of the first subarray
        # We pick the two smallest remaining values as starts of subarrays 2 and 3
        first = second = float('inf')
        
        for i in range(1, len(nums)):
            if nums[i] < first:
                second = first
                first = nums[i]
            elif nums[i] < second:
                second = nums[i]
        
        return nums[0] + first + second