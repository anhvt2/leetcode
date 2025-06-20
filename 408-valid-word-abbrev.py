class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # i for word, j for abbr
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                # If the current character in abbr is a letter, it must match the word
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # If the current character in abbr is a digit, handle it
                if abbr[j] == '0' and (j == 0 or not abbr[j-1].isdigit()):  # no leading zeros
                    return False
                # Extract the number from abbr (could be more than one digit)
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num  # skip the corresponding number of characters in word
        
        # If both pointers have reached the end, it is a valid abbreviation
        return i == len(word) and j == len(abbr)
