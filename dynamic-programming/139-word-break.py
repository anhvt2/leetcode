class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Idea: use dynamic programming to check whether prefixes of s can be built using words in wordDict
        # dp[i] = True if s[0:i] can be segmented using wordDict
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # empty string is always segmentable

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set: # look backward, if s[j:i] in set() then decompose
                    dp[i] = True
                    break
        
        return dp[n]
# Time complexity: O(n**2)
# Space complexity: O(n)