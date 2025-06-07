from typing import List, Optional

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def isPalindrome(ss): # substring
#             n = len(ss)
#             if n == 1: 
#                 return True
#             for i in range(n//2):
#                 if ss[i] != ss[n-1-i]:
#                     return False
#             return True
        
#         # breath-first search: time complexity: O(2**n)
#         def bfs(ss):
#             if len(ss) == 0:
#                 return ''
#             if isPalindrome(ss):
#                 return ss
#             left = bfs(ss[:-1])
#             right = bfs(ss[1:])
#             if len(left) >= len(right):
#                 return left
#             else:
#                 return right

#         return bfs(s)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Initialize pointers
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)     # Odd length palindrome
            len2 = self.expandAroundCenter(s, i, i + 1) # Even length palindrome
            max_len = max(len1, len2)

            if max_len > end - start:
                # Reset pointers position based on discovered max_len
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return right - left - 1  # actual length of the palindrome.
        return (right-1) - (left+1) + 1  # improve readability. note: right += 1, left -= 1, so -1 is for correction


sol = Solution()
# s = "babad"
s = "cbbd"
# s = "babaddtattarrattatddetartrateedredividerb"
print(sol.longestPalindrome(s))

