class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        top, bottom = 0, len(matrix) - 1 # row pointers
        left, right = 0, len(matrix[0]) - 1 # column pointers
        while top <= bottom and left <= right:
            # left to right
            for col in range(left, right+1):
                result.append(matrix[top][col]) # fix row, append col
            top += 1

            # top to bottom
            for row in range(top, bottom+1):
                result.append(matrix[row][right]) # fix col, append row
            right -= 1

            # right to left
            if top <= bottom:
                for col in range(right, left-1, -1):
                    result.append(matrix[bottom][col]) # fix row, append col
                bottom -= 1

            # bottom to top
            if left <= right:
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left]) # fix col, append row
                left += 1
        return result
