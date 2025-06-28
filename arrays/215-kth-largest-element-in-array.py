# Min-Heap (Priority Queue) Approach
#     Maintain a min-heap of size k.
#     Iterate through nums:
#         Add each number to the heap.
#         If the heap size exceeds k, remove the smallest element.
#     At the end, the root of the heap is the kth largest element.

# Time Complexity: O(n log k)
# Space Complexity: O(k)

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k or min_heap[0] < num:
                heapq.heappush(min_heap, num)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)
        return min_heap[0]

# import heapq
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         minheap = []
#         for num in nums:
#             heapq.heappush(minheap, num)
#             if len(minheap) > k:
#                 heapq.heappop(minheap)
#         return minheap[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[-k]

# import random
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
        
#         def quickselect(left, right):
#             # Randomly select a pivot
#             pivot_idx = random.randint(left, right)
#             nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
#             pivot = nums[right]
#             p = left
#             for i in range(left, right):
#                 if nums[i] <= pivot:
#                     nums[i], nums[p] = nums[p], nums[i]
#                     p += 1
#             nums[p], nums[right] = nums[right], nums[p]
#             if p == k:
#                 return nums[p]
#             elif p < k:
#                 return quickselect(p + 1, right)
#             else:
#                 return quickselect(left, p - 1)
        
#         return quickselect(0, len(nums) - 1)
