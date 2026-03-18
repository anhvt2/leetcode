class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        count = 0
        m, n = len(grid), len(grid[0]) # num rows / columns
        # compute a pre-fix sum
        prefix = [[0] * n for _ in range(m)] 

        for i in range(m):
            for j in range(n):
                # current cell value
                prefix[i][j] = grid[i][j]
                # add sum from row above (if exists)
                if i > 0:
                    prefix[i][j] += prefix[i-1][j]
                # add sum from


        for i in range(m):
            for j in range(n):
                if sum(grid[:i][:j]) < k:
                    count += 1
        return count