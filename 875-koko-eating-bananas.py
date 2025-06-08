# Koko eating bananas
from typing import List, Optional

# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         if h < len(piles):
#             return None # cannot finish all the bananas within h hours due to constraints

#         if len(piles) == 1:
#             pile = piles[0]
#             if pile % h == 0:
#                 return piles[0] // h
#             else:    
#                 return piles[0] // h + 1

#         def isFinished(piles: List[int], h: int, k: int):
#             # check if Koko can finish all the bananas within h hours given k
#             total_time = 0
#             for pile in piles:
#                 if pile % k > 0:
#                     total_time += (pile // k + 1)
#                 else:
#                     total_time += (pile // k)
#             if total_time > h:
#                 return False
#             else:
#                 return True

#         # simple binary search
#         left, right = 1, max(piles)*len(piles)/min(h,len(piles))
#         mid = int((left + right) / 2)
#         while not (not isFinished(piles, h, mid) and (isFinished(piles, h, mid+1))):
#             if isFinished(piles, h, mid):
#                 right = mid
#             elif not isFinished(piles, h, mid):
#                 left = mid
#             left, right = int(left), int(right)
#             mid = int((left + right) // 2)

#         k = mid+1
#         return k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left

# piles = [3,6,7,11]
# h = 8
# piles = [30,11,23,4,20]
# h = 6
piles = [1000000000,1000000000]
h = 3
sol = Solution()
result = sol.minEatingSpeed(piles, h)
print(result)
