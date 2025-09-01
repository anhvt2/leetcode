class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])
        
        def place_queen(row, col):
            rows[col] = True
            hills[row - col] = True  # "hill" diagonals
            dales[row + col] = True  # "dale" diagonals
            
        def remove_queen(row, col):
            rows[col] = False
            hills[row - col] = False  # "hill" diagonals
            dales[row + col] = False  # "dale" diagonalsass
            
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack(row + 1, count)
                        
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
                    
            return count
        
        rows = [False] * n
        hills = [False] * (2 * n - 1)  # "hill" diagonals
        dales = [False] * (2 * n - 1)  # "dale" diagonals
        
        return backtrack()