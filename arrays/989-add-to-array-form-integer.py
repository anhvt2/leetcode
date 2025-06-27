class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for d in num:
            n = n * 10 + d
        n = n + k
        res = []
        while n > 0:
            n, r = divmod(n, 10)
            res.append(r)

        return res[::-1]

# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         # Start from the last digit of the num array
#         i = len(num) - 1
#         carry = k
#         result = []
        
#         while i >= 0 or carry > 0:
#             # If there are still digits in the num array, take the digit
#             # otherwise, treat it as 0
#             if i >= 0:
#                 carry += num[i]
            
#             result.append(carry % 10)  # Add the last digit of carry to the result
#             carry //= 10  # Update carry for the next iteration
#             i -= 1  # Move to the next digit
        
#         return result[::-1]  # Reverse the result list to match the correct order
