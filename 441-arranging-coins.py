# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         # The row number is the largest k such that k * (k + 1) / 2 <= n
#         k = 0
#         while (k * (k + 1)) / 2 <= n:
#             k += 1
#         return k - 1  # Subtract 1 because we go one step beyond a valid row

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            i = 0
            count = 0
            while n>=0:
                i += 1
                n -= i
                count += 1
            return count-1

# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         # k*(k+1) / 2 = n
#         # k**2 + k - 2n = 0
#         # k = ( -1 + sqrt( 1 + 8*n  )  ) / 2
#         return int(( -1 + sqrt( 1 + 8*n  )  ) / 2)
