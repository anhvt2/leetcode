class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list to hold the strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False  # Initially, we are going down
        
        # Traverse the string and place characters in the rows
        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down  # Change direction when we reach the first or last row
            current_row += 1 if going_down else -1  # Move down or up
            
        # Concatenate all the rows to form the final result
        return ''.join(rows)

