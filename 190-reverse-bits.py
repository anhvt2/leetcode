class Solution:
    def reverseBits(self, n: int) -> int:
        bit_str32    = format(n, '032b')    # pad (or truncate) to exactly 32 bits
        rev_bit_str  = bit_str32[::-1]
        return int(rev_bit_str, 2)
