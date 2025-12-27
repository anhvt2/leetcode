from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Algorithm:
        ----------
        1. Sort meetings by start time.
        2. Use two heaps:
           - available rooms (min-heap by index)
           - busy rooms (min-heap by end time)
        3. Assign meetings greedily based on room availability.
        4. Count meetings per room.
        5. Return room with highest meeting count.

        Time Complexity: O(m log n)
        Space Complexity: O(n)
        """

        # Sort meetings by start time
        meetings.sort()

        # Min-heap of available rooms
        available = list(range(n))
        heapq.heapify(available)

        # Min-heap of busy rooms: (end_time, room_index)
        busy = []

        # Meeting count per room
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free rooms that have finished before this meeting starts
            while busy and busy[0][0] <= start:
                finish_time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                # Assign to the smallest available room
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # Delay meeting
                finish_time, room = heapq.heappop(busy)
                heapq.heappush(
                    busy,
                    (finish_time + duration, room)
                )

            count[room] += 1

        # Return room with max meetings (tie → smallest index)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
