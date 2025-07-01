class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers and numbers ending with 0 but are not 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # When the number has an odd number of digits, we can discard the middle digit
        return x == reversed_half or x == reversed_half // 10

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x<0:
#             return False
#         elif x==0:
#             return True
#         else:
#             s = str(x)
#             n = len(s)
#             for i in range(n//2+1):
#                 if s[i] != s[n-1-i]:
#                     return False
#             else:
#                 return True
# 
# x = 1000021
# sol = Solution()
# print(sol.isPalindrome(x))
