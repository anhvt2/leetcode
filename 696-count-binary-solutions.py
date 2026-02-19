class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Group string into a group of substrings with identical chars: "00110011" -> ["00", "11", "00", "11"]
        # Valid substrings exist at boundaries of consecutive groups.
        prev = 0      # length of previous group
        curr = 1      # length of current group
        ans = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1 # extend current group
            else:
                ans += min(prev, curr) # Boundary form -> add valid substrings
                # Restart
                prev = curr
                curr = 1
        
        # Handle the last boundary
        ans += min(prev, curr)
        return ans
