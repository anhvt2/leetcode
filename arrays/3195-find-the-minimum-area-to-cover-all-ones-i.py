class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        x_min, x_max, y_min, y_max = float('inf'), float('-inf'), float('inf'), float('-inf')
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    x_min = min(x_min, i)
                    x_max = max(x_max, i)
                    y_min = min(y_min, j)
                    y_max = max(y_max, j)
        return (x_max - x_min + 1) * (y_max - y_min + 1)