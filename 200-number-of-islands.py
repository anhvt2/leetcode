# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m = len(grid) # rows
#         n = len(grid[0]) # cols
#         # Get a list of coord of 1
#         coord_list = []
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     coord_list.append([i,j])

#         numIslands = 0
#         while len(coord_list) > 0:
#             # Initialize
#             pixel = coord_list[0]
#             i,j = pixel[0], pixel[1]
#             coord_list.pop(0)
#             neighbors = [[i,j]]
#             # Perform recursive neighbor search and pop until len(coord_list) = 0
#             isExhausted = False
#             while isExhausted is False:
#                 for k, coord in enumerate(coord_list):
#                     ii, jj = coord[0], coord[1]
#                     for neighbor in neighbors: # Check if [ii, jj] is neighbor with any pixel in neighbors
#                         i,j = neighbor[0], neighbor[1]
#                         if (i==ii and abs(j-jj)==1) or (abs(i-ii)==1 and j==jj): # if found any new neighbor
#                             neighbors.append([ii, jj])
#                             coord_list.pop(k)
#                             isExhausted = False
#                         else: # elif could not find any new neighbor
#                             isExhausted = True
#             print(neighbors)
#             # print(coord_list)
#             numIslands += 1
#         return numIslands

### DFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         m, n = len(grid), len(grid[0])
#         count = 0

#         def dfs(i, j):
#             if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
#                 return
#             grid[i][j] = '0'  # mark visited
#             dfs(i+1, j)  # down
#             dfs(i-1, j)  # up
#             dfs(i, j+1)  # right
#             dfs(i, j-1)  # left

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     dfs(i, j)
#                     count += 1

#         return count


### BFS
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = '0'  # mark as visited

            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        queue.append((nx, ny))
                        grid[nx][ny] = '0'  # mark as visited

        # Loop through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1  # finished one island

        return count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))

