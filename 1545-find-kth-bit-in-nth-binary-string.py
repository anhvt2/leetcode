class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def solve(n, k):
            if n == 1:
                return '0'
            
            mid = 1 << (n - 1)  # 2^(n-1)
            
            if k == mid:
                return '1'
            elif k < mid:
                return solve(n - 1, k)
            else:
                # mirror position
                mirrored = (1 << n) - k
                # invert result
                return '1' if solve(n - 1, mirrored) == '0' else '0'
        
        return solve(n, k)