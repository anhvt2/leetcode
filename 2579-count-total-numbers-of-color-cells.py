class Solution:
    def coloredCells(self, n: int) -> int:
        return 4 * n * (n+1) // 2 - 4 * n + 1 