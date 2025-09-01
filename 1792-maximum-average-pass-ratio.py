from typing import List
import heapq
# Always give the next extra student to the class with the biggest marginal gain:
# \Delta(p,t) = (p+1)/(t+1) - p/t

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # max-heap by pushing negative gain
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1; t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        return sum(p / t for _, p, t in heap) / len(classes)
