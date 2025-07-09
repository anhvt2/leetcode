class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Create DP table with extra row and column initialized to infinity
        dp = [[float('inf') for _ in range (n + 1)] for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1  # base case just outside princess cell

        # Fill DP table from bottom-right to top-left
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, need)  # Health must be at least 1

        return dp[0][0]
