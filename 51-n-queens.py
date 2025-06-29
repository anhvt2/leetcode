class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # This will store all the solutions
        result = []

        # This will track the columns, diagonals, and anti-diagonals that are under attack
        cols = set()  # Tracks columns under attack
        diag1 = set()  # Tracks diagonals (i - j) under attack
        diag2 = set()  # Tracks anti-diagonals (i + j) under attack

        # The board will be represented as a list of strings
        board = [["." for _ in range(n)] for _ in range(n)]

        # Backtracking function to place queens
        def backtrack(row):
            # If we have placed queens in all rows, we have found a solution
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the column or diagonals are under attack
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # Skip if there's a conflict
                
                # Place the queen at the current position
                board[row][col] = "Q"
                # Mark the column and diagonals as under attack
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Recursively place queens in the next row
                backtrack(row + 1)

                # Backtrack: Remove the queen and unmark the attacks
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start the backtracking from the first row
        backtrack(0)

        return result
