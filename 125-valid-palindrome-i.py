# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l = []
#         for i in range(len(s)):
#             if s[i].isalpha() or s[i].isnumeric():
#                 l.append(s[i].lower())
#         for j in range(len(l) // 2):
#             if l[j] != l[-j-1]:
#                 return False
#         return True

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = [char.lower() for char in s if char.isalnum()]
        return filtered == filtered[::-1]