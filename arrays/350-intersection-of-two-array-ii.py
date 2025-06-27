from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the frequency of each element in both arrays
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        # Compute the intersection by taking the minimum frequency of each element in both counters
        intersection = []
        
        for num in counter1:
            if num in counter2:
                # The number of times this element should appear in the intersection
                count = min(counter1[num], counter2[num])
                intersection.extend([num] * count)  # Append the element `count` times
        
        return intersection


# from collections import Counter
# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         counter1 = Counter(nums1)
#         counter2 = Counter(nums2)
#         dup_list = []
#         freqs = []
#         for k1, v1 in counter1.items():
#             if k1 in counter2:
#                 v2 = counter2[k1]
#                 v = min(v1, v2)
#                 dup_list.append(k1)
#                 freqs.append(v)

#         intersection = []
#         for f, n in zip(freqs, dup_list):
#             for i in range(f):
#                 intersection.append(n)
#         return intersection

# # nums1 = [1,2,2,1]; nums2 = [2,2]
