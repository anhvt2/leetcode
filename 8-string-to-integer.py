class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Step 1: Remove leading whitespaces
        
        if not s:
            return 0  # If the string is empty after stripping spaces, return 0
        
        sign = 1  # Default sign is positive
        result = 0  # This will hold the result
        
        # Step 2: Check if there is a sign at the beginning
        if s[0] == '-':
            sign = -1
            s = s[1:]  # Remove the sign
        elif s[0] == '+':
            s = s[1:]  # Remove the sign
        
        # Step 3: Process each character of the string
        for char in s:
            if char.isdigit():  # If the character is a digit
                result = result * 10 + int(char)  # Append the digit to the result
                
                # Step 4: Handle overflow
                if result > 2**31 - 1:
                    return 2**31 - 1 if sign == 1 else -2**31
            else:
                break  # Stop processing when a non-digit character is encountered
        
        # Step 5: Apply the sign and return the result
        return sign * result
