class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Minimum One Bit Operations to Make Integers Zero
        
        Key Insight: This is related to Gray code conversion.
        The answer is the inverse Gray code of n.
        
        Gray code property: consecutive values differ by only 1 bit
        To convert binary to Gray code: gray = n ^ (n >> 1)
        To convert Gray code to binary (inverse): we XOR all bits
        
        Time Complexity: O(log n) - process each bit
        Space Complexity: O(1)
        """
        result = 0
        
        # XOR all bits of n (inverse Gray code)
        while n:
            result ^= n
            n >>= 1
        
        return result