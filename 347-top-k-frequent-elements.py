
# from typing import List, Optional
# from collections import deque, Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = Counter(nums)
#         rank_count = sorted(count.items(), key=lambda x: -x[1]) # naturally small->big, flip order with negative sign
#         topKList = []
#         for i in range(k):
#             values, freqs = rank_count[i] # unpack
#             topKList += [values]
#         return topKList

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        heap = [(-v, k) for k, v in freq.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# import heapq
# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # Count the frequency of each number using Counter
#         freq = Counter(nums)
        
#         # Use heapq.nlargest to get the k elements with the highest frequency
#         # The key used for the heap is the frequency of the number (value)
#         return [item[0] for item in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]



nums = [ 9, 16, 16,  6, 14, 18, 13, 16,  4,  1,  9, 11, 11, 14,  0,  3,  8,
       19,  1,  4,  8, 15,  7,  2,  1, 11,  5, 13,  1, 11, 18, 18,  2, 15,
       16, 10, 19, 10, 19, 18, 13, 12,  5, 14, 18,  1,  7, 14,  5, 17]

sol = Solution()
k = 10
result = sol.topKFrequent(nums, k)
print(result)
