from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort() # sort by start day
        n = len(events)
        i = 0
        day = 0
        count = 0
        minheap = [] # store end days of available events

        # Sweep day by day, always attending event that ends earliest (classic interval scheduling)
        # Use a min-heap of end days:
        #   Push all events whose start <= current day
        #   Pop any day that already ended (end < day)
        #   Attend one (pop the smallest end) and move to the next day
        #   If the heap is empty, then jump to the next day to skip gaps
        
        while i < n or minheap:
            # If no event available, jump to next event's start
            if not minheap:
                day = max(day, events[i][0])

            # Add all events that start on/before 'day'
            while i < n and events[i][0] <= day:
                heapq.heappush(minheap, events[i][1])
                i += 1
            
            # Remove events that have already ended
            while minheap and minheap[0] < day:
                heapq.heappop(minheap)
            
            # Attend one event today (the one that ends earliest)
            if minheap:
                heapq.heappop(minheap)
                count += 1
                day += 1
            
        return count
