class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dynamic programming
        # The minimum number of operations needed to convert the first i characters of word1 to the first j characters of word2.
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # Base Cases
        # dp[0][j] = j: converting empty word1 to first j of word2 = j inserts
        # dp[i][0] = i: converting first i of word1 to empty word2 = i deletes
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    dp[0][j] = j
                elif i > 0 and j == 0:
                    dp[i][0] = i
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1] # char match, no op needed
                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],     # delete
                            dp[i][j-1],     # insert
                            dp[i-1][j-1]    # replace
                        )
        return dp[-1][-1]
