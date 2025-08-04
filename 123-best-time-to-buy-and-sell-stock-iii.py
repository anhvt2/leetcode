from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	# t1_cost: minimal price to pay for the first buy
    	# t1_profit: max profit after first sell
    	# t2_cost: minimal price to pay for the second - first profit
    	# t2_profit: max profit after second sell
    	t1_cost = t2_cost = float('inf')
    	t1_profit = t2_profit = 0
    	for price in prices:
    		# For the first transaction
    		t1_cost = min(t1_cost, price)
    		t1_profit = max(t1_profit, price - t1_cost)

    		# For the second transaction, we reinvest t1_profit, so the effective cost of the second buy is (price - t1_profit)
    		t2_cost = min(t2_cost, price - t1_profit)
    		t2_profit = max(t2_profit, price - t2_cost)

    	return t2_profit
