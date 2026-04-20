import heapq
from collections import Counter
from typing import List
# Time complexity: O(n log k)
# Space: O(n)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = [] # for numbers < median
        min_heap = [] # for numbers > median
        # lazy‐deletion counts
        delayed = Counter()
        # true sizes (excluding delayed)
        max_size = 0
        min_size = 0

        def prune(heap, is_max):
            """Pop and discard top elements marked for deletion."""
            nonlocal delayed
            while heap:
                val = (heap[0][1] if is_max else heap[0])
                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            """Rebalance sizes so that max_size == min_size or max_size == min_size + 1."""
            nonlocal max_size, min_size
            if max_size > min_size + 1:
                # move top of max_heap -> min_heap
                val = heapq.heappop(max_heap)[1]
                max_size -= 1
                heapq.heappush(min_heap, val)
                min_size += 1
                prune(max_heap, is_max=True)
            elif max_size < min_size:
                # move top of min_heap -> max_heap
                val = heapq.heappop(min_heap)
                min_size -= 1
                heapq.heappush(max_heap, (-val, val))
                max_size += 1
                prune(min_heap, is_max=False)

        def add(num):
            """Add a number to one of the heaps."""
            nonlocal max_size, min_size
            if not max_heap or num <= max_heap[0][1]:
                heapq.heappush(max_heap, (-num, num))
                max_size += 1
            else:
                heapq.heappush(min_heap, num)
                min_size += 1
            rebalance()

        def remove(num):
            """Lazily remove a number."""
            nonlocal max_size, min_size
            delayed[num] += 1
            # adjust size counters
            if max_heap and num <= max_heap[0][1]:
                max_size -= 1
                if num == max_heap[0][1]:
                    prune(max_heap, is_max=True)
            else:
                min_size -= 1
                if min_heap and num == min_heap[0]:
                    prune(min_heap, is_max=False)
            rebalance()

        def get_median() -> float:
            """Peek the current median."""
            if max_size > min_size:
                return float(max_heap[0][1])
            return (max_heap[0][1] + min_heap[0]) / 2

        # initialize first window
        for x in nums[:k]:
            add(x)
        result = [get_median()]

        # slide the window
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            result.append(get_median())
        return result

# class Solution:
# Time complexity: n * O(k log k)
# Space: O(n)
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         left, right = 0, k
#         res = []
#         while right < len(nums)+1:
#             arr = sorted(nums[left:right])
#             if k % 2 != 0: # odd
#                 median = float(arr[k//2])
#                 res.append(median)
#             else:
#                 median = 0.5 * (float(arr[k//2-1]) + float(arr[k//2]))
#                 res.append(median)
#             left += 1
#             right += 1
#         return res


# import bisect
# class Solution:
#     def medianSlidingWindow(self, nums, k):
#         w = sorted(nums[:k])
#         res = []
#         for i in range(len(nums)-k+1):
#             # median from middle elements
#             res.append((w[(k-1)//2] + w[k//2]) / 2)
#             # slide window
#             if i < len(nums)-k:
#                 bisect.insort(w, nums[i+k])
#                 w.pop(bisect.bisect_left(w, nums[i]))
#         return res
