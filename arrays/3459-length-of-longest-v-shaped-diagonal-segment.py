from typing import List
from functools import lru_cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Directions in clockwise orer: NE, SE, SW, NW
        dirs = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, turned: bool, need: int, d: int) -> int:
            """
            This function counts the length of the V-shaped diagonal segment.
            If turned == True, then cannot turn anymore.
            If turned == False, then can turn at most once.
            """

            # need is the value we must match at (i,j) where need \in {2, 0}
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if grid[i][j] != need:
                return 0
            
            next_need = 0 if need == 2 else 2
            # continue straight
            dx, dy = dirs[d]
            best = 1 + dfs(i + dx, j + dy, turned, next_need, d)

            # make the single-clockwise turn (once only)
            if not turned: # turned == False
                nd = (d + 1) % 4
                ndx, ndy = dirs[nd]
                best = max(best, 1 + dfs(i + ndx, j + ndy,  True, next_need, nd))
            return best

        # Start only from cells with 1, first step must read as a 2
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d, (dx, dy) in enumerate(dirs):
                        ans = max(ans, 1 + dfs(i + dx, j + dy, False, 2, d))

        return ans