class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # Idea:
        # A rhombus perimeter can be computed quickly using diagonal prefix sums.
        # Two diagonals:
        #   d1: top-left → bottom-right
        #   d2: top-right → bottom-left
        #
        # Each rhombus perimeter consists of 4 diagonal segments.
        # Using prefix sums we compute each segment in O(1).
        # Enumerate all centers and sizes, collect sums, return top 3 distinct.

        m, n = len(grid), len(grid[0])

        # diagonal prefix sums
        d1 = [[0]*(n+1) for _ in range(m+1)]  # TL -> BR
        d2 = [[0]*(n+2) for _ in range(m+1)]  # TR -> BL

        for i in range(m):
            for j in range(n):
                d1[i+1][j+1] = grid[i][j] + d1[i][j]
                d2[i+1][j] = grid[i][j] + d2[i][j+1]

        res = set()

        for r in range(m):
            for c in range(n):
                res.add(grid[r][c])  # size 0 rhombus

                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    # four edges via diagonal prefix sums
                    s1 = d1[r+1][c+k+1] - d1[r-k][c]
                    s2 = d2[r+1][c-k] - d2[r-k][c+1]
                    s3 = d1[r+k+1][c+1] - d1[r][c-k]
                    s4 = d2[r+k+1][c] - d2[r][c+k+1]

                    total = s1 + s2 + s3 + s4 - grid[r-k][c] - grid[r][c+k] - grid[r+k][c] - grid[r][c-k]

                    res.add(total)
                    k += 1

        return sorted(res, reverse=True)[:3]