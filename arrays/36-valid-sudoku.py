class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(subboard: List[str]) -> bool:
            seen = set()
            for element in subboard:
                if element != ".":
                    if element in seen:
                        return False
                    seen.add(element)
            return True

        # Check rows
        for row in board:
            if not isValid(row):
                return False

        # Check columns
        for col in zip(*board):
            if not isValid(col):
                return False

        # Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not isValid(block):
                    return False

        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         m, n = len(board), len(board[0])

#         # define a custom function to check 9 elements
#         def isValid(subboard: List) -> bool:
#             seen = set()
#             for i, element in enumerate(subboard):
#                 if element != ".":
#                     if int(element) in seen:
#                         return False
#                     else:
#                         seen.add(int(element))
#             return True

#         # Check row
#         for i in range(m):
#             row = board[i]
#             if isValid(row) == False:
#                 return False

#         # Check col
#         for j in range(n):
#             col = []
#             for i in range(m):
#                 col.append(board[i][j])
#             if isValid(col) == False:
#                 return False
        
#         # Check 3x3
#         for i in range(0,m,3):
#             for j in range(0,n,3):
#                 sm = []
#                 sm.append(board[i  ][j])
#                 sm.append(board[i+1][j])
#                 sm.append(board[i+2][j])
#                 sm.append(board[i  ][j+1])
#                 sm.append(board[i+1][j+1])
#                 sm.append(board[i+2][j+1])
#                 sm.append(board[i  ][j+2])
#                 sm.append(board[i+1][j+2])
#                 sm.append(board[i+2][j+2])
#                 if isValid(sm) == False:
#                     return False
#         return True
