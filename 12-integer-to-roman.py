class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the Roman numeral mappings for each place value
        roman_numerals = [
            ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),   # ones
            ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),   # tens
            ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),   # hundreds
            ("", "M", "MM", "MMM")  # thousands
        ]
        
        # Convert the number to Roman numeral
        result = ""
        place = 0
        
        while num > 0:
            # Get the current digit in the place value (ones, tens, hundreds, thousands)
            digit = num % 10
            result = roman_numerals[place][digit] + result
            num //= 10  # Remove the last digit
            place += 1
        
        return result
