class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Initialize the minimum price as a very large value
        max_profit = 0  # Initialize the maximum profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price if a new lower price is found
            else:
                max_profit += price - min_price  # Add the profit from the difference between price and min_price
                min_price = price  # Update min_price to the current price after selling
        
        return max_profit


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
        
#         # Iterate through prices and accumulate profit when price increases
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 max_profit += prices[i] - prices[i - 1]  # Sell at prices[i] after buying at prices[i - 1]
        
#         return max_profit


