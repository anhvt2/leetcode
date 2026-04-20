# Space complexity: O(n)
# Time complexity: O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        max_seen = 0
        # Walk from the rightmost building to the left
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_seen:
                res.append(i)
                max_seen = heights[i]
        # We collected indices in descending order, so reverse before returning
        return res[::-1]

# class Solution:
#     def findBuildings(self, heights: List[int]) -> List[int]:
#         res = []
#         heights = heights[::-1] # flip the ocean to the left
#         reqd_height = float('-inf')
#         for i, height in enumerate(heights):
#             if height > reqd_height: # need to be taller to have ocean view
#                 res.append((len(heights)-1)-i)
#                 reqd_height = max(reqd_height, height)
#         return res[::-1] # more efficient than sorted(res)