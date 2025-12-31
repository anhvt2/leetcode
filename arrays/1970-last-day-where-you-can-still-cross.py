from typing import List
from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        Algorithm:
        ----------
        1. Binary search on the last day we can cross.
        2. For a given day d:
           - Mark the first d cells as water.
           - BFS from all land cells in the top row.
           - Check if bottom row is reachable.
        3. Return the maximum valid day.

        Time Complexity: O((row * col) * log(row * col))
        Space Complexity: O(row * col)
        """

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_cross(day: int) -> bool:
            # Build grid: 0 = land, 1 = water
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1

            q = deque()

            # Start BFS from all land cells in the top row
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = 1  # mark visited

            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

            return False

        left, right = 0, row * col
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
