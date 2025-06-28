from collections import deque, Counter
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)  # Number of rows in the board
        m = len(board[0])  # Number of columns in the board
        
        # Early termination: if the word is longer than the number of cells in the board, it's impossible to find
        if len(word) > m * n:
            return False
        
        count = Counter(sum(board, []))  # Count frequency of each letter in the board

        # Check if any letter in the word is missing or appears too few times in the board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
        
        # If the first letter appears less frequently than the last letter in the board,
        # reverse the word to optimize search (this reduces unnecessary searches)
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        del count  # Delete the count object since it's no longer needed
        
        # Initialize visited matrix with -1 (unvisited cells)
        visited = [[-1] * m for i in range(n)]
        
        # Define a backtrack function that performs DFS to check if the word can be formed starting from a cell
        def backtrack(board, i, j, index):
            if index == len(word):  # If all characters in word have been matched
                return True

            # Explore the four possible directions (right, down, left, up)
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ii = i + dx  # New row index
                jj = j + dy  # New column index
                # Check if the new indices are valid (within bounds of the board)
                if ii > -1 and ii < n and jj > -1 and jj < m:
                    # Ensure the cell is unvisited and matches the character in the word at the current index
                    if visited[ii][jj] == -1 and board[ii][jj] == word[index]:
                        visited[ii][jj] = 1  # Mark the cell as visited
                        # Continue searching with the next character in the word
                        if backtrack(board, ii, jj, index + 1):
                            return True
                        visited[ii][jj] = -1  # Unmark the cell if the search fails
            return False  # Return false if no valid path was found

        # Loop through each cell in the board and start the search if the first character of the word is found
        for i in range(0, n):
            for j in range(0, m):
                if board[i][j] == word[0]:  # If the current cell matches the first character of the word
                    visited[i][j] = 1  # Mark as visited
                    if backtrack(board, i, j, 1):  # Start DFS from here
                        return True
                    visited[i][j] = -1  # Backtrack and unmark the cell
        return False  # Return false if no valid path was found after searching all cells


# from collections import deque
# from typing import List

# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         m = len(board)
#         n = len(board[0])
        
#         # Directions to move in the grid (right, left, down, up)
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
#         # Backtracking DFS function to search the word
#         def dfs(i, j, index):
#             # If we've checked all characters of the word
#             if index == len(word):
#                 return True
            
#             # Check boundaries and if the current cell matches the word[index]
#             if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
#                 return False
#             else: # Search for next char in word
#                 # Temporarily mark the current cell as visited by replacing it with a special character
#                 temp = board[i][j]
#                 board[i][j] = '#'
                
#                 # Explore all four directions (right, left, down, up)
#                 for di, dj in directions:
#                     ni, nj = i + di, j + dj
#                     if dfs(ni, nj, index + 1):  # Recursive call for the next character in the word
#                         return True
            
#                 # Backtrack, restore the original character in the cell
#                 board[i][j] = temp
#             return False
        
#         # Iterate over every cell in the board
#         for i in range(m):
#             for j in range(n):
#                 # Start DFS if the first character matches the word's first character
#                 if board[i][j] == word[0]:
#                     if dfs(i, j, 0):  # Start DFS with index 0 of the word
#                         return True
        
#         return False
