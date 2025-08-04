from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        t_cost  = [float('inf')] * k
        t_profit = [0] * k
        for price in prices:
            for i in range(k):
                if i == 0:
                    # For the first transaction
                    t_cost[i] = min(t_cost[i], price)
                    t_profit[i] = max(t_profit[i], price - t_cost[i])
                else: # i > 0
                    # For the ith transaction, we reinvest t_profit[i-1], so the effective cost of the ith buy is (price - t_profit[i-1])
                    t_cost[i] = min(t_cost[i], price - t_profit[i-1])
                    t_profit[i] = max(t_profit[i], price - t_cost[i])

        return t_profit[-1]
