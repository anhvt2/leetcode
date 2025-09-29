from typing import List

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        # len is the interval length
        for length in range(3, n+1):           # need at least 3 vertices
            for i in range(0, n - length + 1):
                j = i + length - 1
                best = float('inf')
                for k in range(i+1, j):
                    best = min(best, dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
                dp[i][j] = best
        return dp[0][n-1]
