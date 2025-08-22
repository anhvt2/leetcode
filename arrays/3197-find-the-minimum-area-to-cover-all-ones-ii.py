from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count(dir1, dir2):
            dp = [[0]*len(grid[0]) for _ in range(len(grid))]
            up = [len(grid)]*len(grid[0])
            down = [-1]*len(grid[0])
            for i in dir1(range(len(grid))):
                l, r, u, d = len(grid[0]), -1, len(grid), -1
                for j in dir2(range(len(grid[0]))):
                    if grid[i][j]:
                        up[j] = min(up[j], i)
                        down[j] = max(down[j], i)
                    u = min(u, up[j])
                    d = max(d, down[j])
                    if down[j] >= 0:
                        l = min(l, j)
                        r = max(r, j)
                    dp[i][j] = (r-l+1)*(d-u+1) if r >= 0 else 0
            return dp
        
        def count2(is_vertical):
            def get_n():
                return len(grid) if not is_vertical else len(grid[0])

            def get_m():
                return len(grid[0]) if not is_vertical else len(grid)

            def get(i, j):
                return grid[i][j] if not is_vertical else grid[j][i]
    
            left = [get_m() for _ in range(get_n())]
            right = [-1 for _ in range(get_n())]
            for i in range(get_n()):
                for j in range(get_m()):
                    if get(i, j) == 0:
                        continue
                    left[i] = min(left[i], j)
                    right[i] = max(right[i], j)
            dp = [[0]*get_n() for _ in range(get_n())]
            for i in range(len(dp)):
                l, r, u, d = get_m(), -1, get_n(), -1
                for j in range(i, len(dp[0])):
                    if right[j] != -1:
                        l = min(l, left[j])
                        r = max(r, right[j])
                        u = min(u, j)
                        d = max(d, j)
                    dp[i][j] = (r-l+1)*(d-u+1) if r >= 0 else 0
            return dp

        up_left = count(lambda x: x, lambda x: x)
        up_right = count(lambda x: x, reversed)
        down_left = count(reversed, lambda x: x)
        down_right = count(reversed, reversed)
        horizon = count2(False)
        vertical = count2(True)
        result = float("inf")
        for i in range(len(grid)-1):
            for j in range(len(grid[0])-1):
                result = min(result,
                             up_left[i][j]+up_right[i][j+1]+horizon[i+1][len(grid)-1],
                             horizon[0][i]+down_left[i+1][j]+down_right[i+1][j+1],
                             up_left[i][j]+down_left[i+1][j]+vertical[j+1][len(grid[0])-1],
                             vertical[0][j]+up_right[i][j+1]+down_right[i+1][j+1])
        for i in range(len(grid)-2):
            for j in range(i+1, len(grid)-1):
                result = min(result, horizon[0][i]+horizon[i+1][j]+horizon[j+1][len(grid)-1])
        for i in range(len(grid[0])-2):
            for j in range(i+1, len(grid[0])-1):
                result = min(result, vertical[0][i]+vertical[i+1][j]+vertical[j+1][len(grid[0])-1])
        return result
