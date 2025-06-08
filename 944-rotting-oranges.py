from typing import List, Optional

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         # 0: empty cell
#         # 1: fresh
#         # 2: rotten
#         m, n = len(grid), len(grid[0])
#         mins = 0
#         def dfs(i, j):
#             if (i < 0 or i >= m or 
#                 j < 0 or j >= n or 
#                 mins > m*n):
#                 return
            
#             if grid[i-1][j] == 1 and i>0: grid[i-1][j] = 2
#             if grid[i+1][j] == 1 and i<m-1: grid[i-1][j] = 2
#             if grid[i][j-1] == 1 and j>0: grid[i][j-1] = 2
#             if grid[i][j+1] == 1 and j<n-1: grid[i][j+1] = 2
#             mins += 1
#             # Spread to neighbors
#             dfs(i, j+1)
#             dfs(i, j-1)
#             dfs(i+1, j)
#             dfs(i-1, j)
#             return

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 2:
#                     # print(f"Rot starts from ({i}, {j})") # need ground zero for igniting
#                     dfs(i,j)

#                 return mins

from collections import deque

class Solution():
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Collect all starting points for rotten oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0)) # (row, column, minute)
                elif grid[i][j] == 1:
                    fresh += 1

        mins = 0
        directions = [(-1,0), (+1,0), (0,-1), (0,+1)] # down, up, left, right
        while queue:
            i, j, mins = queue.popleft()
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh -= 1
                    queue.append((ni, nj, mins+1))

        if fresh == 0:
            return mins
        else:
            return -1


grid = [[2,1,1],[1,1,0],[0,1,1]]
sol = Solution()
result = sol.orangesRotting(grid)
print(result)
