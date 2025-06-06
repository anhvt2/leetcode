from typing import List, Optional
from collections import deque

# Intuition: find V shape (monotonically decreasing followed by monotonically increasing)

from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         total_water = 0

#         def expand_left(i):
#             if i == 0 or height[i] >= height[i - 1]:
#                 return [i]
#             return expand_left(i - 1) + [i]

#         def expand_right(i):
#             if i == n - 1 or height[i] >= height[i + 1]:
#                 return [i]
#             return [i] + expand_right(i + 1)

#         for i in range(1, n - 1):
#             if height[i - 1] > height[i] and height[i] < height[i + 1]:
#                 # Found a valley
#                 left = expand_left(i)
#                 right = expand_right(i)
#                 valley = left[:-1] + right  # merge, avoid duplicate center
#                 if len(valley) < 3:
#                     continue  # need at least 3 bars to trap water

#                 left_wall = height[valley[0]]
#                 right_wall = height[valley[-1]]
#                 water_level = min(left_wall, right_wall)

#                 # Compute water for this valley
#                 for idx in valley[1:-1]:  # exclude boundary walls
#                     trapped = max(0, water_level - height[idx])
#                     total_water += trapped

#         return total_water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1

        return total_water


        
height = [0,1,0,2,1,0,1,3,2,1,2,1] # [[1,0,2], [2,1,0,1,3], [2,1,2]]
sol = Solution()
print(sol.trap(height))
