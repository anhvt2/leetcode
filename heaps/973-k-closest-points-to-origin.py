import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a max-heap to store the k closest points
        max_heap = []
        
        # Iterate over each point
        for x, y in points:
            # Calculate the squared Euclidean distance from the origin
            dist = x * x + y * y
            
            # Push the point into the max-heap with the negative of the distance to simulate a max-heap
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # If the heap size exceeds k, remove the farthest point (the one with the largest negative distance)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        # Extract the points from the heap and return them (they are already the closest k points)
        return [point for (dist, point) in max_heap]
