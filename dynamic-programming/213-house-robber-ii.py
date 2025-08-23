class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])

        # For more than two houses, at each house i, you have two choices:
        # 1. Rob the current house i and add its value to the maximum money robbed up to house i-2.
        # 2. Skip the current house and take the maximum money robbed up to house i-1.
        # Idea: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # Can rob nums[0..n-2] or nums[1..n-1]

        def rob_line(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]

        return max(rob_line(nums[0:n-1]), rob_line(nums[1:n]))


