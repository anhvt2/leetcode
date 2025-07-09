class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Initialize 9 sets for rows, cols, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Step 1: Fill sets with existing digits and find empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        # Step 2: Recursive backtracking
        def backtrack(index):
            if index == len(empty):
                return True  # Solved

            r, c = empty[index]
            b = (r // 3) * 3 + c // 3  # box index

            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    # Place digit
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    # Recurse
                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)

            return False

        backtrack(0)


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         def is_valid(r, c, d):
#             block_row, block_col = 3 * (r // 3), 3 * (c // 3)
#             for i in range(9):
#                 if board[r][i] == d: return False  # row check
#                 if board[i][c] == d: return False  # col check
#                 # 3x3 box check
#                 if board[block_row + i // 3][block_col + i % 3] == d:
#                     return False
#             return True

#         def backtrack():
#             for r in range(9):
#                 for c in range(9):
#                     if board[r][c] == '.':
#                         for d in map(str, range(1, 10)):
#                             if is_valid(r, c, d):
#                                 board[r][c] = d
#                                 if backtrack():
#                                     return True
#                                 board[r][c] = '.'  # backtrack
#                         return False  # no valid number
#             return True  # fully filled and valid

#         backtrack()


# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         # Helper function to check if placing digit d at (r, c) is valid
#         def is_valid(r, c, d):
#             block_row, block_col = 3 * (r // 3), 3 * (c // 3)
#             for i in range(9):
#                 if board[r][i] == d: return False  # Check row
#                 if board[i][c] == d: return False  # Check column
#                 # Check 3x3 sub-box
#                 if board[block_row + i // 3][block_col + i % 3] == d:
#                     return False
#             return True

#         # Recursive backtracking function to fill the board
#         def backtrack():
#             for r in range(9):
#                 for c in range(9):
#                     # If the cell is empty, try to fill it
#                     if board[r][c] == '.':
#                         # Try digits '1' through '9'
#                         for d in map(str, range(1, 10)):
#                             if is_valid(r, c, d):
#                                 board[r][c] = d  # Place digit
#                                 if backtrack():  # Recurse
#                                     return True  # If successful, return immediately
#                                 board[r][c] = '.'  # Backtrack (undo move)
#                         # If no valid digit found, return False to trigger backtrack
#                         return False
#             # If no empty cells remain, board is solved
#             return True

#         # Start backtracking from the first cell
#         backtrack()
