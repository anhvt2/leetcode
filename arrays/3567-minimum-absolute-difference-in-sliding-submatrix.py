class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        if k == 1:
            return [[0]*n for _ in range(m)]
        
        res = [[0]*(n-k+1) for _ in range(m-k+1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []
                
                # collect k×k elements
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])
                
                # distinct values only
                vals = sorted(set(vals))
                
                # FIX: if < 2 distinct values → diff = 0
                if len(vals) < 2:
                    res[i][j] = 0
                    continue
                
                # compute min adjacent diff
                min_diff = float('inf')
                for t in range(1, len(vals)):
                    min_diff = min(min_diff, vals[t] - vals[t-1])
                
                res[i][j] = min_diff
        
        return res