from sortedcontainers import SortedList
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # General ideas:
        # 1. request i (ideally) should be assigned to server (i % k)
        # 2. if server (i % k) is busy, then try (i+1 % k), (i+2 % k), ...
        # 3. if all servers are busy, drop request
        # Approach: min-heap + TreeSet (or SortedList)
        # 1. min-heap (end_time, server_index)
        # 2. sorted set of available servers
        busy = [] # min-heap: (end_time, server_index)
        free = SortedList(range(k)) # initially all servers are free
        request_count = [0] * k # request counts per server

        for i, (start, duration) in enumerate(zip(arrival, load)):
            # Step 1: Free up any servers that have completed by now
            while busy and busy[0][0] <= start:
                end_time, server = heapq.heappop(busy)
                free.add(server)
            
            if not free:
                continue # all servers busy, drop request
            
            # Step 2: Find the first available server >= i % k
            idx = free.bisect_left(i % k)
            if idx == len(free):
                idx = 0 # wrap around

            server = free[idx]
            free.remove(server)
            heapq.heappush(busy, (start + duration, server))
            request_count[server] += 1

        max_request_count = max(request_count)
        return [i for i, c in enumerate(request_count) if c == max_request_count]
