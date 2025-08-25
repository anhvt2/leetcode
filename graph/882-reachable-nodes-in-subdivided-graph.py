# Complexity: O((N+E) log(N))
import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Dijkstra algorithm

        # Build adjacency
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w+1))
            g[v].append((u, w+1))
        
        # Dijkstra from node 0
        dist = [float(inf)] * n
        dist[0] = 0
        pq = [(0, 0)] # (dist, node)
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, cost in g[u]:
                nd = d + cost
                if nd < dist[v] and nd <= maxMoves + (cost-1):
                    # The + (cost-1) bound is optimal, it's a small prune
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        # 1) orignal nodes reachable
        ans = sum(1 for d in dist if d <= maxMoves)

        # 2) subdivided nodes per edge
        for u, v, w in edges:
            a = 0 if dist[u] == float('inf') else max(0, maxMoves - dist[u])
            b = 0 if dist[v] == float('inf') else max(0, maxMoves - dist[v])
            ans += min(w, a+b)
        return ans
