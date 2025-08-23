from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # # For more than two houses, at each house i, you have two choices:
        # # 1. Rob the current house i and add its value to the maximum money robbed up to house i-2.
        # # 2. Skip the current house and take the maximum money robbed up to house i-1.
        # # Idea: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # Time complexity: O(n)
        # Space complexity: O(1) -- very obscure: two pointers tracking previous and current indices
        # prev2 = 0  # dp[i-2]
        # prev1 = nums[0]  # dp[i-1]
        
        # # Iterate through the list starting from the second index
        # for i in range(1, len(nums)):
        #     prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        # return prev1
        
        # # The result will be stored in prev1 (dp[n-1])

        # Time complexity: O(n)
        # Space complexity: O(n)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
