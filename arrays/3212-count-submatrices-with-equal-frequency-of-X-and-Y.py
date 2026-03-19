class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix sums for X and Y
        px = [[0]*(n+1) for _ in range(m+1)]
        py = [[0]*(n+1) for _ in range(m+1)]
        
        # build prefix sums
        for i in range(m):
            for j in range(n):
                px[i+1][j+1] = px[i][j+1] + px[i+1][j] - px[i][j]
                py[i+1][j+1] = py[i][j+1] + py[i+1][j] - py[i][j]
                
                if grid[i][j] == 'X':
                    px[i+1][j+1] += 1
                elif grid[i][j] == 'Y':
                    py[i+1][j+1] += 1
        
        res = 0
        
        # enumerate all bottom-right corners
        for i in range(m):
            for j in range(n):
                countX = px[i+1][j+1]
                countY = py[i+1][j+1]
                
                # check conditions
                if countX == countY and countX > 0:
                    res += 1
        
        return res