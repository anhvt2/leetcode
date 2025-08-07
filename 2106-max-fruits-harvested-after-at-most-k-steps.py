from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        max_fruits = 0                # Tracks the best total fruits collected so far
        left = 0                      # Left index of our sliding window over `fruits`
        total = 0                     # Sum of fruits within the current window [left..right]

        # Expand the window's right boundary one fruit position at a time
        for right in range(len(fruits)):
            total += fruits[right][1]  # Include fruits at the new rightmost position

            # Shrink the window from the left until the interval [left_pos..right_pos]
            # can be visited within k steps (with at most one turn)
            while left <= right:
                left_pos = fruits[left][0]    # Position of the leftmost fruit in window
                right_pos = fruits[right][0]  # Position of the rightmost fruit in window

                # Two possible routes to sweep the entire window:
                # 1) Go from startPos -> left_pos, then traverse to right_pos
                dist_left_first = abs(startPos - left_pos) + (right_pos - left_pos)
                # 2) Go from startPos -> right_pos, then traverse back to left_pos
                dist_right_first = abs(startPos - right_pos) + (right_pos - left_pos)

                # If either route fits within k steps, window is valid
                if min(dist_left_first, dist_right_first) <= k:
                    break  # No need to shrink further

                # Otherwise, drop the leftmost fruit out of the window and retry
                total -= fruits[left][1]
                left += 1

            # Update the maximum fruits collected among all valid windows
            max_fruits = max(max_fruits, total)

        return max_fruits      # Return the best total found


# from typing import List
# import bisect
# class Solution:
#     def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
#         # (1) Extract position and build prefix sums of fruit counts
#         positions = [p for p, _ in fruits]
#         n = len(fruits)
#         prefix = [0] * n
#         prefix[0] = fruits[0][1]
#         for i in range(1,n):
#             prefix[i] = prefix[i-1] + fruits[i][1]

#         def collect(l: int, r: int) -> int:
#             """Sum fruits on all positions in [l..r]"""
#             i = bisect.bisect_left(positions, l)
#             j = bisect.bisect_right(positions, r) - 1
#             if i > j:
#                 return 0
#             else:
#                 return prefix[j] - (prefix[i-1] if i else 0)
            
#         ans = 0
#         # Case A: go left x, then back to start, then right remaining
#         # you spend 2*x steps coming back, so right range is startPos..startPos+(k-2x)
#         for x in range(0, k//2+1):
#             leftmost = startPos - x
#             rightmost = startPos + (k - 2*x)
#             ans = max(ans, collect(leftmost, rightmost))
        
#         # Case B: go right x, then back, then left remaining
#         for x in range(0, k//2 + 1):
#             rightmost = startPos + x
#             leftmost = startPos - (k - 2*x)
#             ans = max(ans, collect(leftmost, rightmost))
        
#         return ans