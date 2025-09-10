from typing import 
from collections import defaultdict
import heapq

def findCheapestWithPath(n: int, flights: List[List[int]], src: int, dst: int) -> int, List[int]:

    g = defaultdict(list)
    for u, v, w in flights:
        g[u].append((v, w))

    pq = [(0, src)]
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[src] = 0

    while pq:
        cost, u = heapq.heappop(pq)
        if u == dst:
            # reconstruct path
            path = []
            cur = dst
            while cur != -1:
                path.append(cur)
                cur = parent[cur]
            return cost, path[::-1]
        if cost > dist[u]:
            continue
        for v, w in g[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                parent[v] = u
                heapq.heappush(pq, (nc, v))
    return -1, []
