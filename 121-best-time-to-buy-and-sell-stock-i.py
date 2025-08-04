# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxProfit = 0 # initialize
#         for i in range(len(prices)-1, 0, -1): # selling date
#             for j in range(i-1, -1, -1): # buying date
#                 maxProfit = max(maxProfit, prices[i] - prices[j])
#         return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # update the lowest price seen so far
            else:
                max_profit = max(max_profit, price - min_price)  # update profit if better

        return max_profit

        
prices = [7,1,5,3,6,4]
sol = Solution()
result = sol.maxProfit(prices)
print(result)
