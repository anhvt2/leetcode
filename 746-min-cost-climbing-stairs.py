from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        elif n == 2:
            return min(cost[0], cost[1])
        
        # minCost[i] is the min cost to reach step i
        minCost = [0] * n
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        
        for i in range(2, n):
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        
        # Final step can be reached from either of the last two stairs
        return min(minCost[n-1], minCost[n-2])
