from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        Treat each row as the base of a histogram.
        Apply Largest Rectangle in Histogram for each row.
        """

        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            # Build histogram heights for current row
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Compute max rectangle area for this histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Standard monotonic stack solution for histogram.
        """
        stack = []
        max_area = 0

        # Add sentinel to flush stack
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # remove sentinel
        return max_area
