from typing import List
import heapq
from collections import defaultdict

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int) -> int:
    # Build adjacency list: u -> list of (v, w)
    g = defaultdict(list)
    for u, v, w in flights:
        g[u].append((v, w))

    # min-heap of (total_cost_so_far, node)
    pq = [(0, src)]
    # best known cost to each node
    dist = [float('inf')] * n
    dist[src] = 0

    while pq:
        cost, u = heapq.heappop(pq)
        if u == dst:
            return cost                         # earliest pop of dst is optimal
        if cost > dist[u]:
            continue                            # stale entry
        for v, w in g[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    return -1                                    # unreachable

