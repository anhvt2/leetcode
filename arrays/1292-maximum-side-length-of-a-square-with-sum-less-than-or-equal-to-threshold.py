from typing import List
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """
        Optimized version using Binary Search
        Time: O(m*n*log(min(m,n)))
        Space: O(m*n)
        """
        m, n = len(mat), len(mat[0])
        
        # Build 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + prefix[i-1][j] + 
                               prefix[i][j-1] - prefix[i-1][j-1])
        
        def can_find_square(side_length):
            """Check if there exists a square of given side_length with sum <= threshold"""
            for i in range(side_length, m + 1):
                for j in range(side_length, n + 1):
                    # Sum of square ending at (i-1, j-1) with side_length
                    square_sum = (prefix[i][j] - 
                                 prefix[i-side_length][j] - 
                                 prefix[i][j-side_length] + 
                                 prefix[i-side_length][j-side_length])
                    if square_sum <= threshold:
                        return True
            return False
        
        # Binary search for maximum valid side length
        left, right = 0, min(m, n)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_find_square(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result