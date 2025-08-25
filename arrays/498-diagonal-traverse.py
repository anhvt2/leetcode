from typing import List

# # ---- First solution
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         m, n = len(mat), len(mat[0])
#         l = []
#         for sum in range(m+n-1):
#             tmp = []
#             for i in range(m):
#                 j = sum - i
#                 if 0 <= j < n:
#                     tmp.append(mat[i][j])
#             if sum % 2 == 0:
#                 tmp.reverse()
#             l.extend(tmp)
#         return l

# # ---- Second solution
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = 0, 0
        m, n = len(mat), len(mat[0])
        ans = []
        for _ in range(m*n):
            ans.append(mat[row][col])
            
            if (row + col) % 2 == 0:
                if col == n-1: # hit right boundary
                    row += 1
                elif row == 0: # hit top boundary
                    col += 1
                else:
                    row -= 1
                    col += 1

            else: # (row + col) % 2 = 1

                if row == m - 1: # hit bottom boundary
                    col += 1 
                elif col == 0: # hit left boundary
                    row += 1
                else:
                    row += 1
                    col -= 1
        return ans