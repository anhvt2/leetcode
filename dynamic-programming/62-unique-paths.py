class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # From any cell (i, j) can only arrive from left (i-1, j) or top (i, j-1)
        # dp[i,j] = dp[i-1,j] + dp[i,j-1]
        
        dp = [[1 for i in range(n)] for j in range(m)]
        # Base cases
        for j in range(n):
            dp[0][j] = 1 # 1 way in the first row
        for i in range(m):
            dp[i][0] = 1 # 1 way in the first column
        # O(m*n)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[i][j]

# O(1) both time and space complexity
# from math import comb
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return comb(m+n-2, m-1)
# # Total moves = (m - 1) downs and (n - 1) rights. Choose m-1 down moves from (m + n - 2) total moves.