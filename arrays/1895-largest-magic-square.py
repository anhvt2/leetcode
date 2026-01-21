from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        """
        Algorithm:
        - Use prefix sums for rows, columns, and diagonals
        - Check squares from largest size to smallest
        """

        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag = [[0] * (n + 1) for _ in range(m + 1)]
        anti = [[0] * (n + 1) for _ in range(m + 1)]

        # Build prefix sums
        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag[i + 1][j + 1] = diag[i][j] + grid[i][j]
                anti[i + 1][j] = anti[i][j + 1] + grid[i][j]

        # Try sizes from large to small
        for size in range(min(m, n), 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    target = row[i][j + size] - row[i][j]

                    # Check rows
                    if any(
                        row[i + r][j + size] - row[i + r][j] != target
                        for r in range(size)
                    ):
                        continue

                    # Check columns
                    if any(
                        col[i + size][j + c] - col[i][j + c] != target
                        for c in range(size)
                    ):
                        continue

                    # Check main diagonal
                    if diag[i + size][j + size] - diag[i][j] != target:
                        continue

                    # Check anti-diagonal
                    if anti[i + size][j] - anti[i][j + size] != target:
                        continue

                    return size

        return 1
