class Solution:
    def clearDigits(self, s: str) -> str:
        # Convert the string to a list to easily modify characters
        s = list(s)

        # Iterate until there are no digits left or no valid pairs to remove
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                # Find the closest non-digit character to the left of the current digit
                j = i - 1
                while j >= 0 and s[j].isnumeric():
                    j -= 1

                # If there's a non-digit character to the left of the current digit
                if j >= 0 and s[j].isalpha():
                    # Remove the digit at i and the non-digit character at j
                    s.pop(i)  # Remove digit at i
                    s.pop(j)  # Remove non-digit character at j
                    i = max(j - 1, 0)  # Move the pointer back to check the next characters
                else:
                    i += 1
            else:
                i += 1

        # Convert the list back to a string and return it
        return ''.join(s)
