class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1  # Initialize max_diff to -1, as per problem statement
        i = 0
        
        # Iterate through the array to find the maximum difference
        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                max_diff = max(max_diff, nums[j] - nums[i])
            else:
                i = j  # Move `i` to `j` if we find a smaller value, so that `nums[j]` can be larger than `nums[i]`
        
        return max_diff
