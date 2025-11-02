class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        Expand around the center (optimal space)

        Every palindrome has a center. A center can be:
        - A single char (odd-length palindrome)
        - Between two chars (even-length palindrome)

        Total centers: n chars + (n-1) gaps = 2n - 1 possible centers
        """
        def expand_around_center(left, right):
            # Count number of palindrome given a center
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1 # Found a palindrome
                left -= 1
                right += 1
            
            return count
    
        total = 0
        for i in range(len(s)):
            # Odd-length palindrome (center is a char)
            total += expand_around_center(i, i)
            # Even-length palindrome (center is a gap between 2 chars)
            total += expand_around_center(i, i+1)
        
        return total
