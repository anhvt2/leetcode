from typing import List, Optional


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: empty cell
        # 1: fresh
        # 2: rotten
        mins = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (grid[i][j] != 0) or (grid[i][j] != 1):
                return
            grid[i][j] = 2
            mins += 1

            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        dfs
