from collections import deque
from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_list = []  # List to store valid points
        distances = []  # List to store distances of valid points
        idxs = []  # List to store the indices of valid points

        # Iterate through the points and find valid ones (either x or y should match)
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                valid_list.append(point)
                distances.append(abs(point[0] - x) + abs(point[1] - y))  # Manhattan distance
                idxs.append(i)

        # If no valid points are found, return -1
        if not valid_list:
            return -1

        # Find the index of the point with the smallest distance
        min_distance = min(distances)  # Find the minimum distance
        min_index = distances.index(min_distance)  # Get the index of that minimum distance
        
        # Return the index from idxs that corresponds to the minimum distance
        return idxs[min_index]
