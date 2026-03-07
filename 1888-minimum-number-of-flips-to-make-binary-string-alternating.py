class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  # allow rotations via sliding window
        
        diff1 = 0  # mismatches with "0101..."
        diff2 = 0  # mismatches with "1010..."
        
        res = float('inf')
        
        for i in range(len(s)):
            # expected chars for both alternating patterns
            c1 = '0' if i % 2 == 0 else '1'
            c2 = '1' if i % 2 == 0 else '0'
            
            if s[i] != c1:
                diff1 += 1
            if s[i] != c2:
                diff2 += 1
            
            # shrink window when size > n
            if i >= n:
                c1 = '0' if (i-n) % 2 == 0 else '1'
                c2 = '1' if (i-n) % 2 == 0 else '0'
                
                if s[i-n] != c1:
                    diff1 -= 1
                if s[i-n] != c2:
                    diff2 -= 1
            
            # evaluate window of size n
            if i >= n - 1:
                res = min(res, diff1, diff2)
        
        return res