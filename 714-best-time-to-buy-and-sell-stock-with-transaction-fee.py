from typing import List
# dynamic programming
# hold: max profit holding a stock at day i
# cash: max profit not holding a stock at day i
# at day i, if buy: hold = max(hold, cash - prices[i])
# at day i, if sell: cash = max(cash, hold + prices[i] - free)

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         cash = 0 # The profit if we are not holding any stock at day 0
#         hold = -prices[0] # The profit if we are holding a stock at day 0

#         for price in prices[1:]:
#             # Sell
#             cash = max(cash, hold + price - fee)
#             # Buy
#             hold = max(hold, cash - price)
        
#         return cash

# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         buy = float("-inf")
#         sell = 0

#         for price in prices:
#             buy = max(buy, sell - price)
#             sell = max(sell, buy + price - fee)

#         return sell

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 'buy': effective cost to buy a stock (including fee and subtracting current profit).
        # 'sell': maximum profit achieved so far
        buy = float('inf')  # Start with an infinitely high cost (we haven't bought yet)
        sell = 0            # No profit initially

        for price in prices:
            # Consider if buying today would result in a better effective cost
            # price + fee - sell represents the real cost to buy today:
            # price + fee: the raw cost to buy
            # - sell: use current profit to offset the cost (buy with profit)
            if price + fee - sell < buy:
                buy = price + fee - sell  # Update to the cheaper buy price

            # Consider if selling today gives more profit
            # price - buy is the potential profit if we bought at 'buy' and sell at today's price
            sell = max(sell, price - buy)  # Update max profit if this sell is better

        # At the end, 'sell' contains the maximum profit after all days
        return sell
