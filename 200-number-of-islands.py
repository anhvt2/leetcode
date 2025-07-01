# ### BFS
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def bfs(i, j):
            # Build a list of to-be-visited pixels
            queue = deque()
            queue.append((i, j))
            grid[i][j] = '0'  # mark as visited

            while queue:
                ii, jj = queue.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # down, up, left, right
                    ni, nj = x + di, y + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        queue.append((ni, nj))
                        grid[ni][nj] = '0'  # mark as visited

        # Loop through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1  # finished one island

        return count

## DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'  # mark visited
            dfs(i+1, j)  # down
            dfs(i-1, j)  # up
            dfs(i, j+1)  # right
            dfs(i, j-1)  # left

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


# Time complexity: O(m*n)
# Space complexity: O(m*n)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))

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
#                     for neighbor in neighbors: # Check if [ii, jj] is neighbor with anj pixel in neighbors
#                         i,j = neighbor[0], neighbor[1]
#                         if (i==ii and abs(j-jj)==1) or (abs(i-ii)==1 and j==jj): # if found anj new neighbor
#                             neighbors.append([ii, jj])
#                             coord_list.pop(k)
#                             isExhausted = False
#                         else: # elif could not find anj new neighbor
#                             isExhausted = True
#             print(neighbors)
#             # print(coord_list)
#             numIslands += 1
#         return numIslands
