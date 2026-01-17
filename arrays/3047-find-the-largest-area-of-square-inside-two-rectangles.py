class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        """
        Find the largest square area that fits in the intersection of any two rectangles.
        
        Algorithm:
        1. Enumerate all pairs of rectangles
        2. For each pair, calculate the intersection rectangle
        3. If intersection exists, find the largest square that fits
        4. Track the maximum square area
        """
        max_area = 0
        n = len(bottomLeft)
        
        # Check all pairs of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Get coordinates of rectangle i
                x1, y1 = bottomLeft[i]
                x2, y2 = topRight[i]
                
                # Get coordinates of rectangle j
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]
                
                # Calculate intersection rectangle
                # Bottom-left corner: max of bottom-left corners
                inter_x1 = max(x1, x3)
                inter_y1 = max(y1, y3)
                
                # Top-right corner: min of top-right corners
                inter_x2 = min(x2, x4)
                inter_y2 = min(y2, y4)
                
                # Calculate width and height of intersection
                width = inter_x2 - inter_x1
                height = inter_y2 - inter_y1
                
                # If valid intersection exists (positive width and height)
                if width > 0 and height > 0:
                    # Largest square has side = min(width, height)
                    side = min(width, height)
                    area = side * side
                    max_area = max(max_area, area)
        
        return max_area