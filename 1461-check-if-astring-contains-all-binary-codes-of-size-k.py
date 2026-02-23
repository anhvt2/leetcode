class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k               # total possible binary codes = 2^k
        seen = set()
        
        mask = 0                    # rolling integer representation
        all_ones = need - 1         # keeps only k bits
        
        for i, ch in enumerate(s):
            # shift left and add current bit
            mask = ((mask << 1) & all_ones) | (ch == '1')
            
            if i >= k - 1:          # window size reached k
                seen.add(mask)
                if len(seen) == need:
                    return True     # early exit
        
        return False