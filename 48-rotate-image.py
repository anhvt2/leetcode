class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Idea:
        (1) Transpose
        (2) Reverse columns
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for rows in matrix:
            rows.reverse()

        return 



# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# out = 
# [[7,4,1],[8,5,2],[9,6,3]]

