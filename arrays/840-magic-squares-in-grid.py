from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        Algorithm:
        ----------
        1. Iterate over all possible 3x3 subgrids.
        2. For each subgrid:
           - Ensure the center is 5.
           - Ensure numbers are exactly 1 through 9.
           - Ensure all rows, columns, and diagonals sum to 15.
        3. Count valid magic squares.

        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """

        m, n = len(grid), len(grid[0])
        count = 0

        # Iterate over all possible 3x3 centers
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if self.is_magic(grid, i, j):
                    count += 1

        return count

    def is_magic(self, grid: List[List[int]], i: int, j: int) -> bool:
        """
        Check if the 3x3 grid centered at (i, j) is a magic square.
        """

        # Center must be 5
        if grid[i][j] != 5:
            return False

        nums = set()
        for r in range(i - 1, i + 2):
            for c in range(j - 1, j + 2):
                val = grid[r][c]
                if val < 1 or val > 9:
                    return False
                nums.add(val)

        # Must contain exactly numbers 1 through 9
        if len(nums) != 9:
            return False

        # Check rows
        for r in range(i - 1, i + 2):
            if sum(grid[r][j - 1:j + 2]) != 15:
                return False

        # Check columns
        for c in range(j - 1, j + 2):
            if grid[i - 1][c] + grid[i][c] + grid[i + 1][c] != 15:
                return False

        # Check diagonals
        if grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] != 15:
            return False
        if grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1] != 15:
            return False

        return True
