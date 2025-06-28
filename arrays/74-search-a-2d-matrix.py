# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         lst = [item for row in matrix for item in row]
#         return True if target in lst else False

# Idea: binary search for row, find the row, then binary search again within the row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Step 1: Binary search to find the correct row
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:  # target is within this row's range
                # Step 2: Binary search within the row
                row_left, row_right = 0, len(matrix[mid]) - 1
                while row_left <= row_right:
                    row_mid = (row_left + row_right) // 2
                    if matrix[mid][row_mid] == target:
                        return True
                    elif matrix[mid][row_mid] < target:
                        row_left = row_mid + 1
                    else:
                        row_right = row_mid - 1
                return False  # target is not found in this row
            elif matrix[mid][0] < target:
                left = mid + 1  # Target might be in a row with larger values
            else:
                right = mid - 1  # Target might be in a row with smaller values
        
        return False  # Target not found in any row
