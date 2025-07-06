from collections import deque
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        
        # Initialize smooth_img with zeros, ensuring separate rows
        smooth_img = [[0] * n for _ in range(m)]

        # Directions to check (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for i in range(m):
            for j in range(n):
                neighbors = deque([(i, j)])    # Start with the current pixel
                
                # Add neighbors
                for di, dj in directions:
                    ii, jj = i + di, j + dj
                    if 0 <= ii < m and 0 <= jj < n:
                        neighbors.append((ii, jj))

                # Calculate sum of neighbor values and count
                total = 0
                count = len(neighbors)
                for ii, jj in neighbors:
                    total += img[ii][jj]

                # Assign the average value to the smoothed image
                smooth_img[i][j] = total // count    # Use integer division

        return smooth_img
