# At any moment:
#     Each element in the heap corresponds to one room that's currently in use.
#     The smallest end time is always at heap[0] — this tells you which meeting ends the soonest.

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min-heap to track end times
        heap = []
        for interval in intervals:
            start, end = interval
            
            if heap and heap[0] <= start: # reuse room if first ending <= next
                heapq.heappop(heap)
            
            # Allocate new room
            heapq.heappush(heap, end)
        
        return len(heap)
