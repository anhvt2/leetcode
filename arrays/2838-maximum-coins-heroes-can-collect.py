# class Solution:
#     def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
#         n = len(heroes)
#         m = len(monsters) # len(coins)
        
#         ans = []
#         for i in range(n):
#             # ans[i] = coins[j] where j = argmax_{j in 0..n} monsters[j] <= heroes[i]
#             # curr_max_coin = float('-inf')
#             curr_sum = 0
#             for j in range(m):
#                 if monsters[j] <= heroes[i]:
#                     curr_sum += coins[j]
#             ans.append(curr_sum)
#         return ans
                    
from typing import List
import bisect

class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        # sort monsters by strength and build prefix sum of coins
        pairs = sorted(zip(monsters, coins))
        if not pairs:
            return [0] * len(heroes)
        ms, cs = zip(*pairs)              # sorted monsters and their coins
        pref = [0]
        for c in cs:
            pref.append(pref[-1] + c)     # pref[i] = sum of first i coins

        # for each hero h, take all monsters with ms <= h
        ans = []
        for h in heroes:
            i = bisect.bisect_right(ms, h)  # count of monsters <= h
            ans.append(pref[i])             # sum of their coins
        return ans

