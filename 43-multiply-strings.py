class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Implement a int() function
        def to_int(num1 : str):
            r = 0
            n = len(num1)
            for c in num1:
                r += char_to_int[c] * 10 ** (n - 1)
                n -= 1
            return r

        digits = "0123456789"
        char_to_int = {}
        for i, c in enumerate(digits):
            char_to_int[c] = i
        
        return str(to_int(num1) * to_int(num2))
