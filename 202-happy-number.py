# class Solution:
#     def isHappy(self, n: int) -> bool:
#         # len(str(n)) - 1
#         s = str(n)
#         summ = 0
#         while summ != 1:
#             for i in range(len(s)):
#                 summ += int(s[i])**2    
#             if summ == 1:
#                 return True
#             s = str(summ)
#             summ = 0
#         return False

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To track previously seen sums
        while n != 1:
            if n in seen:  # If we've seen this number before, we're in a cycle
                return False
            seen.add(n)
            # Calculate the sum of the squares of the digits of n
            n = sum(int(digit) ** 2 for digit in str(n))
        return True


sol = Solution()
print(sol.isHappy(19))
