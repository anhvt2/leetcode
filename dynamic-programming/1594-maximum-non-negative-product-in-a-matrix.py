class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Idea: Track both max and min products at each cell (since negative × negative = positive)
        # Use DP where dp_max[i][j] and dp_min[i][j] store max/min products to reach (i,j)
        
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp_max[i][j] = maximum product path from (0,0) to (i,j)
        # dp_min[i][j] = minimum product path from (0,0) to (i,j)
        dp_max = [[float('-inf')] * n for _ in range(m)]
        dp_min = [[float('inf')] * n for _ in range(m)]
        
        # Base case: starting cell
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        
        # Fill first row (can only come from left)
        for j in range(1, n):
            dp_max[0][j] = dp_min[0][j] = dp_max[0][j-1] * grid[0][j]
        
        # Fill first column (can only come from top)
        for i in range(1, m):
            dp_max[i][0] = dp_min[i][0] = dp_max[i-1][0] * grid[i][0]
        
        # Fill rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                # Can come from top or left
                # Current cell value
                val = grid[i][j]
                
                # All possible products (from top-max, top-min, left-max, left-min)
                candidates = [
                    dp_max[i-1][j] * val,  # from top (max path)
                    dp_min[i-1][j] * val,  # from top (min path, important if val is negative)
                    dp_max[i][j-1] * val,  # from left (max path)
                    dp_min[i][j-1] * val   # from left (min path, important if val is negative)
                ]
                
                dp_max[i][j] = max(candidates)
                dp_min[i][j] = min(candidates)
        
        # Result is the max product at bottom-right
        result = dp_max[m-1][n-1]
        
        # Return -1 if result is negative (as per problem requirement)
        return result % MOD if result >= 0 else -1