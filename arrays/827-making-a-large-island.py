from typing import List
from collections import deque

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        # 1) Label islands starting from id=2 (since grid has 0/1)
        area = {0: 0}       # area[id] = size; define 0->0 for convenience
        curr_id = 2

        def bfs(sr: int, sc: int, idv: int) -> int:
            q = deque([(sr, sc)])
            grid[sr][sc] = idv
            size = 1
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = idv
                        size += 1
                        q.append((nr, nc))
            return size

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[curr_id] = bfs(r, c, curr_id)
                    curr_id += 1

        # If there was at least one island, start with its max area; else 0
        ans = max(area.values()) if len(area) > 1 else 0

        # 2) Try flipping each 0 and compute merged area of distinct neighboring islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    total = 1  # flip this 0 to 1
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            idv = grid[nr][nc]
                            if idv > 1 and idv not in seen:
                                seen.add(idv)
                                total += area[idv]
                    ans = max(ans, total)

        # Edge case: all zeros -> we can flip one to get area 1
        return max(ans, 1 if ans == 0 else ans)
