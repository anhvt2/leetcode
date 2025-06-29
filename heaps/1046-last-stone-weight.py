
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones list to a max-heap (in Python, heapq is a min-heap, so we negate the values to simulate max-heap)
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pop the two largest stones (which are the smallest when negated)
            first = - heapq.heappop(heap)
            second = - heapq.heappop(heap)
            
            if first > second:
                heapq.heappush(heap, -(first - second))
        
        # If the heap is empty, return 0. Otherwise, return the last remaining stone.
        return -heap[0] if heap else 0


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         if len(stones) == 0:
#             return 0
#         elif len(stones) == 1:
#             return stones[0]
#         while len(stones) > 1:
#             stones.sort()
#             last = stones.pop()
#             next_last = stones.pop()
#             stones.append(last - next_last)
#             if len(stones) == 0:
#                 return 0
#             elif len(stones) == 1:
#                 return stones[0]

