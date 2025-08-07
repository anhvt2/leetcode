from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        # (1) Sum along the main diagonal
        first = sum(fruits[i][i] for i in range(n))

        # (2) Top-right → bottom-right (dirs: (1,-1),(1,0),(1,1))
        dp2 = [[float('-inf')]*n for _ in range(n)]
        dp2[0][n-1] = fruits[0][n-1]
        for x in range(1, n):
            for y in range(n):
                # only allow positions strictly above diagonal, or the target
                if x >= y and not (x == n-1 and y == n-1):
                    continue
                best = float('-inf')
                # from (x-1, y+1), (x-1, y), (x-1, y-1)
                for dx, dy in [( -1, +1 ), ( -1, 0 ), ( -1, -1 )]:
                    px, py = x+dx, y+dy
                    if 0 <= px < n and 0 <= py < n:
                        best = max(best, dp2[px][py])
                if best > float('-inf'):
                    dp2[x][y] = best + fruits[x][y]
        second = dp2[n-1][n-1]

        # (3) Bottom-left -> bottom-right (directions: (-1,1),(0,1),(1,1))
        dp3 = [[float('-inf')]*n for _ in range(n)]
        dp3[n-1][0] = fruits[n-1][0]
        for y in range(1, n):
            for x in range(n):
                # only allow positions strictly below diagonal, or the target
                if x <= y and not (x == n-1 and y == n-1):
                    continue
                best = float('-inf')
                # from (x+1, y-1), (x, y-1), (x-1, y-1)
                for dx, dy in [( +1, -1 ), ( 0, -1 ), ( -1, -1 )]:
                    px, py = x+dx, y+dy
                    if 0 <= px < n and 0 <= py < n:
                        best = max(best, dp3[px][py])
                if best > float('-inf'):
                    dp3[x][y] = best + fruits[x][y]
        third = dp3[n-1][n-1]

        # (4) Combine and subtract double-counted last cell
        return first + second + third - 2*fruits[n-1][n-1]
