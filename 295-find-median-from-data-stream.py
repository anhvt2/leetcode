import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # for numbers > median
        self.max_heap = [] # for numbers < median
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            # Move smallest number in large array to small array
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap):
            # Move largest number in small array to large array
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()