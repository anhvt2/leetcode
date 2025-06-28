from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with a value greater than the amount (inf)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # No coins needed to make amount 0
        
        # Iterate over all amounts from 1 to the target amount
        for i in range(1, amount + 1):
            for coin in coins: # this loop ensures to exhaust all possible options and choose the optimal one
                if i - coin >= 0:  # If the current amount is greater than or equal to the coin value
                    dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum of the previous dp value and the new one
                
        # If dp[amount] is still inf, it's not possible to form the amount with the given coins
        return dp[amount] if dp[amount] != float('inf') else -1
