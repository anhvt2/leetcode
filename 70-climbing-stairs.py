class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: 1 way to climb 1 step, 2 ways to climb 2 steps
        if n == 1:
            return 1
        if n == 2:
            return 2

        # prev_one: ways to reach the previous step (n-1)
        # prev_two: ways to reach two steps before (n-2)
        prev_two = 1   # ways to reach step 1
        prev_one = 2   # ways to reach step 2

        # Calculate number of ways for each step from 3 to n
        for current_step in range(3, n + 1):
            current_ways = prev_one + prev_two  # total ways to reach current step
            prev_two = prev_one                 # update for next iteration
            prev_one = current_ways

        return prev_one  # this is the result for n steps
