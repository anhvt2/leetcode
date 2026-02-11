class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Count total 'a's to the right
        a_right = s.count('a')
        b_left = 0
        result = a_right  # Delete all 'a's
        
        for ch in s:
            if ch == 'a':
                a_right -= 1
            else:  # ch == 'b'
                b_left += 1
            
            # Min deletions = delete b's on left OR a's on right
            result = min(result, b_left + a_right)
        
        return result