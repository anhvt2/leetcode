from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # ---- First Solution
        if desiredTotal==0:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)<2*desiredTotal:
            return False
        if maxChoosableInteger*(maxChoosableInteger+1)in {2*desiredTotal,2*desiredTotal-1}:
            return bool(maxChoosableInteger%2)
        memo={}
        def win(T,a):
            if T[-1]>=a:
                return True
            tt=tuple(T)
            if tt in memo:
                return memo[tt]
            if a<=0:
                memo[tt]=False
                return False
            res=False
            for i in range(len(T)):
                if win(T[:i]+T[i+1:],a-T[i])==False:
                    res=True
                    break
            memo[tt]=res
            return res
        return win([a for a in range(1,maxChoosableInteger+1)],desiredTotal)

        # # ---- Second Solution
        # # Edge case: (1) first player already wins at beginning
        # if desiredTotaliredTotal <= 0:
        #     return True
        # # Edge case: (2) impossible for anyone to reach
        # total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        # if total_sum < desiredTotaliredTotal:
        #     return False

        # # Return True if current player can force a win: Complexity O(2**maxChoosableInteger)
        # @lru_cache(None)
        # def dfs(used_mask: int, remain: int) -> bool:
        #     # Try picking a number i from 1..maxChoosableInteger
        #     for i in range(1, maxChoosableInteger + 1):
        #         # bit = 1 << (i - 1)
        #         bit = 2**i
        #         if used_mask & bit:
        #             continue  # already taken
        #         # If picking i wins immediately, or makes opponent lose later
        #         if i >= remain or not dfs(used_mask | bit, remain - i):
        #             return True
        #     return False

        # return dfs(0, desiredTotaliredTotal)
