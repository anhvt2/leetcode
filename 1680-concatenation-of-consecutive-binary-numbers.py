class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        
        ans = 0
        bits = 0  # current bit length
        
        for i in range(1, n + 1):
            # if i is power of 2 → bit length increases
            if i & (i - 1) == 0:
                bits += 1
            
            # shift left to make space, then append i
            ans = ((ans << bits) + i) % MOD
        
        return ans