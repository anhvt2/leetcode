from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d2, max_area = float('-inf'), float('-inf')

        for i, [w, l] in enumerate(dimensions):
            d2 = w**2 + l**2
            area = w*l
            if d2 > max_d2:
                max_d2 = d2
                max_area = area
            elif d2 == max_d2:
                max_area = max(area, max_area)
        return max_area
        