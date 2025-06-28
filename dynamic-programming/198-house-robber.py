from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # For more than two houses, at each house i, you have two choices:
        # 1. Rob the current house i and add its value to the maximum money robbed up to house i-2.
        # 2. Skip the current house and take the maximum money robbed up to house i-1.
        # Idea: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # Initialize the first two values of the DP array
        prev2 = 0  # dp[i-2]
        prev1 = nums[0]  # dp[i-1]
        
        # Iterate through the list starting from the second index
        for i in range(1, len(nums)):
            current = max(prev1, prev2 + nums[i])  # Max of robbing or not robbing the current house
            prev2 = prev1  # Move prev1 to prev2
            prev1 = current  # Move current to prev1
        
        # The result will be stored in prev1 (dp[n-1])
        return prev1
