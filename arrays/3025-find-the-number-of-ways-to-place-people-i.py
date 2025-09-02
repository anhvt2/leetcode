from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Idea: sort points by x ascending, and for equal y, descending
        # For each left point i = (x_i, y_i), scan points to its right (j > i) keeping the current best (highest) y we have already paired, maxY
        # We can form a valid pair (i, j) iff
        #   * y_i >= y_j (i is the upper-left corner)
        #   * y_j > maxY (ensure no other point inside/on the rectangle)
        # then set maxY = y_j and continue. 
        # Complexity: O(n**2)

        points.sort(key=lambda p: (p[0], -p[1]))

        count = 0
        for i, (_, yi) in enumerate(points):
            maxY = float('-inf')
            for j in range(i+1, len(points)):
                yj = points[j][1]
                if yi >= yj > maxY:
                    count += 1
                    maxY = yj
        return count