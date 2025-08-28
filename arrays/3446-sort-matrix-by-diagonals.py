from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for d in range(-n+1, n):
            idxs = []
            vals = []
            for i in range(n):
                j = i + d
                if 0 <= j < n:
                    idxs.append((i, j))
                    vals.append(grid[i][j])
            
            if i >= j:
                vals.sort(reverse=True) # if bottom-left (diagonal included) -> non-ascending order
            else:
                vals.sort(reverse=False) # if top-right -> ascending order

            for (i, j), v in zip(idxs, vals):
                grid[i][j] = v

        return grid
