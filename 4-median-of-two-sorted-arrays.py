from typing import List
# import numpy as np

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums1, num2 = np.array(nums1), np.array(nums2)
#         tmp = np.hstack((nums1, nums2))
#         return np.median(tmp)

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merged = sorted(nums1 + nums2)
#         n = len(merged)
#         if n % 2 == 1:
#             return float(merged[n // 2])
#         else:
#             return (merged[n // 2 - 1] + merged[n // 2]) / 2

class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        # Always binary search the smaller array for efficiency
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        low, high = 0, m

        # Binary search on the smaller array A
        while low <= high:
            i = (low + high) // 2          # Partition A
            j = (m + n + 1) // 2 - i       # Partition B to balance left/right sides

            # Get border values around partition i in A
            maxLeftA = float('-inf') if i == 0 else A[i - 1]
            minRightA = float('inf') if i == m else A[i]

            # Get border values around partition j in B
            maxLeftB = float('-inf') if j == 0 else B[j - 1]
            minRightB = float('inf') if j == n else B[j]

            # Valid partition condition: left side maxes ≤ right side mins
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                # If total length is even, median is average of two middle values
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    # Odd case: median is max of left side
                    return float(max(maxLeftA, maxLeftB))
            elif maxLeftA > minRightB:
                # Too far right in A; move partition left
                high = i - 1
            else:
                # Too far left in A; move partition right
                low = i + 1

A = [1,3]
B = [2]
sol = Solution()
result = sol.findMedianSortedArrays(A, B)
print(result)
