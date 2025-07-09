class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        
        # Mapping from digits to corresponding letters
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        # Backtracking function to build combinations
        def backtrack(index, current_combination):
            # If the current combination is of the same length as digits, add it to result
            if index == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters for the current digit
            letters = digit_to_letters[digits[index]]
            
            # Explore each letter for the current digit
            for letter in letters:
                # Add the letter to the current combination and recurse
                current_combination.append(letter)
                backtrack(index + 1, current_combination)
                # Backtrack (remove the last letter)
                current_combination.pop()
        
        # Start backtracking from index 0 with an empty current combination
        backtrack(0, [])
        
        return result
