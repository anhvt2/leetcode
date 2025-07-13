class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area between the left and right pointers
            width = right - left
            current_area = min(height[left], height[right]) * width
            
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
