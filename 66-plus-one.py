
from typing import List, Optional

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the digits from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # Return once hit any number < 9
            digits[i] = 0  # Set current digit to 0 if there's a carry
            
        # If all digits are 9, we need to add a 1 at the beginning
        return [1] + digits


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits[-1] += 1
#         digits.reverse()
#         for i in range(len(digits)):
#             if digits[i] > 9 and i < len(digits)-1:
#                 digits[i] = 0
#                 digits[i+1] += 1
#             elif digits[i] > 9 and i == len(digits)-1:
#                 digits[i] = 0
#                 digits.append(1)
#         digits.reverse()
#         return digits

# # this is a joke - do not present this during interview
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         x = 0
#         for i in range(len(digits)):
#             x += digits[i] * 10**(len(digits)-i-1)
#         lists = []
#         s = str(x+1)
#         for i in range(len(s)):
#             lists.append(int(s[i]))
#         return lists

digits = [9,9]
sol = Solution()
print(sol.plusOne(digits))
