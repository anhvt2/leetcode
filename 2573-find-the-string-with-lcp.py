from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        c = ord('a') - 1  # Start before 'a'
        word = [None] * n  # Initialize with None instead of non-letter char
        
        # Construct candidate string by assigning letters
        for i in range(n):
            if word[i] is not None:  # Already has a candidate letter
                continue
            
            c += 1  # Move to next letter
            if c > ord('z'):  # Ran out of letters (more than 26 distinct chars needed)
                return ""
            
            # Assign current letter to all positions with lcp[i][j] > 0
            for j in range(i, n):
                if lcp[i][j] > 0:
                    word[j] = chr(c)
        
        # Validate if the constructed word matches the lcp matrix
        for i in range(n):
            for j in range(n):
                # Calculate what lcp[i][j] should be based on word
                next_lcp = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                curr_lcp = 1 + next_lcp if word[i] == word[j] else 0
                
                # Check if it matches the given lcp value
                if lcp[i][j] != curr_lcp:
                    return ""
        
        return ''.join(word)