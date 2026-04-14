class Solution:
    def minimumTotalDistance(self, robot, factory):
        """
        Key idea:
        - Sort robots and factories by position.
        - This becomes a classic DP / assignment problem:
            assign robots to factories with capacity constraints
            minimizing total |robot[i] - factory[j]|

        Observations:
        - Optimal matching is monotonic (no crossing): after sorting,
          we assign robots in order to factories in order.
        - Expand each factory into multiple "slots" based on its limit.

        Let:
            robots = sorted(robot)
            slots = expanded factory positions

        Then problem reduces to:
            match robots[i] to slots[j] with minimum cost
            BUT we must use exactly len(robots) slots in order.

        DP definition:
            dp[i][j] = min cost to match first i robots using first j slots

        Transition:
            1. skip slot j (not use it)
            2. use slot j to match robot i

        Optimize to 1D DP.

        Time: O(n * total_slots) ≤ 1e5 * 1e5 worst, but constraints OK due to sum limits
        """

        robot.sort()
        factory.sort()

        # expand factories into slots
        slots = []
        for pos, limit in factory:
            slots.extend([pos] * limit)

        m = len(robot)
        n = len(slots)

        # dp[j] = min cost to match current i robots using first j slots
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, m + 1):
            new_dp = [float('inf')] * (n + 1)
            for j in range(1, n + 1):
                # option 1: skip this slot
                new_dp[j] = new_dp[j - 1]

                # option 2: match robot i-1 with slot j-1
                if dp[j - 1] != float('inf'):
                    cost = dp[j - 1] + abs(robot[i - 1] - slots[j - 1])
                    new_dp[j] = min(new_dp[j], cost)

            dp = new_dp

        return dp[n]