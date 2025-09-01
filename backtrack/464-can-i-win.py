from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Quick prunes
        if desiredTotal <= 0:
            return True
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(used_mask: int, remain: int) -> bool:
            # Try picking a number i from 1..maxChoosableInteger
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if used_mask & bit:
                    continue  # already taken
                # If picking i wins immediately, or makes opponent lose later
                if i >= remain or not dfs(used_mask | bit, remain - i):
                    return True
            return False

        return dfs(0, desiredTotal)
