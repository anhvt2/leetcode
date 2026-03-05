class Solution:
    def minOperations(self, s: str) -> int:
        mismatch = 0  # mismatches vs pattern "0101..."
        
        for i, c in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if c != expected:
                mismatch += 1
        
        # At every position the two target patterns differ:
        #   "0101..." vs "1010..."
        # Therefore a position that matches one pattern must mismatch the other.
        # If m positions mismatch "0101...", then exactly (n - m) mismatch "1010...".
        return min(mismatch, len(s) - mismatch)