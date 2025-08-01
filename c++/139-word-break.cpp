#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        int n = s.length();
        vector<bool> dp(n+1, false);
        dp[0] = true; // empty string = true

        for (int i = 0; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordSet.count(s.substr(j, i-j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};