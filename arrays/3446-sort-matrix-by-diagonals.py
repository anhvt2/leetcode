from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # iterate over all main diagonals: d = i - j, from -(n-1) .. (m-1)
        for d in range(-(n - 1), m):
            idxs = []
            vals = []
            # collect cells on this diagonal
            for i in range(m):
                j = i - d
                if 0 <= j < n:
                    idxs.append((i, j))
                    vals.append(grid[i][j])

            # sort direction per triangle:
            # bottom-left (including main): d >= 0 -> non-increasing
            # top-right: d < 0 -> non-decreasing
            if d >= 0:
                vals.sort(reverse=True)   # non-increasing
            else:
                vals.sort()               # non-decreasing

            # write back along the same diagonal
            for (i, j), v in zip(idxs, vals):
                grid[i][j] = v

        return grid
