from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Check if START or END is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # Special case:
        if n == 1:
            return 1

        # 8 directions, right, left, down, up, and 4 diagonals
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0), # right, left, down, up 
            (1, 1), (1, -1), (-1, 1), (-1, -1) # diagonals
        ]

        # BSF initialization
        queue = deque([(0, 0, 1)]) # (row, col, distance)
        grid[0][0] = 1 # Mark as visited

        while queue:
            row, col, dist = queue.popleft()

            # Try all 8 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check if we reached the destination
                if new_row == n - 1 and new_col == n - 1:
                    return dist + 1

                # Check bounds and if cell is valid(0) and not visited
                if (0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0):
                    queue.append((new_row, new_col, dist + 1))
                    grid[new_row][new_col] = 1 # Marked as visited

        return -1 # No path found
