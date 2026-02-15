class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Idea: Simulate binary addition from right to left with carry
        # Start from the least significant bit (rightmost)
        
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get current bits (0 if index out of bounds)
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Add bits + carry
            total = bit_a + bit_b + carry
            result.append(str(total % 2))  # Current bit
            carry = total // 2              # Carry for next position
            
            i -= 1
            j -= 1
        
        # Result is built backwards, reverse it
        return ''.join(reversed(result))