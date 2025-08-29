from typing import List
from collections import deque

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # For each building, BFS over reachable empty cells; add the path length to dist and increment reach. After processing all buildings, pick the empty cell that every building reached (reach == B) with the smallest dist. If none qualifies, return -1.
# Time: O(Bmn). Space: O(mn)
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])

        # dist[r][c]: total distance from all buildings that reached (r,c)
        # reach[r][c]: how many buildings reached (r,c)
        dist = [[0]*n for _ in range(m)]
        reach = [[0]*n for _ in range(m)]

        buildings = [(r, c) for r in range(m) for c in range(n) if grid[r][c] == 1]
        B = len(buildings)
        if B == 0:
            return -1

        # grid = 
        # [[1 0 2 0 1]
        #  [0 0 0 0 0]
        #  [0 0 1 0 0]]
        # dist[0]       # dist[1]       # dist[2]
        # [[0 1 0 5 0]  # [[0 5 0 1 0]  # [[0 3 0 3 0]
        #  [1 2 3 4 5]  #  [5 4 3 2 1]  #  [3 2 1 2 3]
        #  [2 3 0 5 6]] #  [6 5 0 3 2]] #  [2 1 0 1 2]]
        # sum over dist yields the cell with min distance to all buildings

        # BFS from each building
        for br, bc in buildings:
            q = deque([(br, bc, 0)])
            visited = [[False]*n for _ in range(m)]
            visited[br][bc] = True # start at an arbitrary building

            while q:
                r, c, d = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        if grid[nr][nc] == 0:  # empty land
                            dist[nr][nc] += d + 1
                            reach[nr][nc] += 1
                            q.append((nr, nc, d + 1))
                        # if it's 1 or 2, we don't go through

        # Find the minimum sum distance among cells reached by all buildings
        ans = min(
            (dist[r][c] for r in range(m) for c in range(n)
             if grid[r][c] == 0 and reach[r][c] == B),
            default=float('inf')
        )
        return -1 if ans == float('inf') else ans
