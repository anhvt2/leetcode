from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # stop -> list of route indices that serve this stop
        stop_to_routes = defaultdict(list)
        for r, stops in enumerate(routes):
            for s in stops:
                stop_to_routes[s].append(r)

        # Initialize BFS with all routes that we can board at 'source'
        q = deque()
        visited_route = set()
        for r in stop_to_routes[source]:
            q.append(r)
            visited_route.add(r)

        buses = 1  # taking any of these routes counts as 1 bus

        # If any starting route already reaches target directly
        for r in list(q):
            if target in set(routes[r]):
                return buses

        # BFS over routes via shared stops
        while q:
            for _ in range(len(q)):
                r = q.popleft()
                # For every stop this route serves, consider all routes that also serve it
                for s in routes[r]:
                    for nr in stop_to_routes[s]:
                        if nr in visited_route:
                            continue
                        # If the neighboring route contains target, done
                        if target in set(routes[nr]):
                            return buses + 1
                        visited_route.add(nr)
                        q.append(nr)
                    # Optional micro-optimization: clear list to avoid revisiting same stop
                    stop_to_routes[s] = []
            buses += 1

        return -1
