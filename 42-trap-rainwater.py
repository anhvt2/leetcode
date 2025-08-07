from typing import List, Optional
from collections import deque

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1       # Two pointers at both ends
        left_max, right_max = 0, 0             # Track max height seen so far from each side
        total_water = 0                        # Accumulated trapped water

        # Move pointers toward each other
        while left < right:
            # Always move the smaller side inward:
            if height[left] < height[right]:
                # If current bar on left is new max, update left_max
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Otherwise, water can be trapped above this bar
                    total_water += left_max - height[left]
                left += 1
            else:
                # Symmetric logic for the right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water

    
height = [0,1,0,2,1,0,1,3,2,1,2,1] # [[1,0,2], [2,1,0,1,3], [2,1,2]]
sol = Solution()
print(sol.trap(height))
