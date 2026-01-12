from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Algorithm:
        - For each consecutive pair of points,
          add the Chebyshev distance between them.
        """

        total_time = 0

        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            # Distance in x and y directions
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            # Minimum time to move between the two points
            total_time += max(dx, dy)

        return total_time
