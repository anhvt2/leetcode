# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # Bellman-Ford algorithm (can also consider Djikstra algorithm and shortest path algorithm)
#         # 1. Init cost array dp of length n with float('inf'), except dp[src] = 0
#         # 2. Iterate k+1 times (k stops or nodes -> k+1 edges)
#         #   * copy tmp = dp[:]
#         #   * for each flight (u, v, w), if dp[u] + w < tmp[v], then tmp[v] = dp[u] + w
#         #   * at the end, set dp = tmp
#         # 3. After k+1 iterations, dp[dst] holds the min cost at most K stops (or float('inf') if unreachable)
#         # time complexity: O((k+1)x(n+E))
#         # space: O(n)
#         dp =  [float('inf')] * n
#         dp[src] = 0

#         for _ in range(k+1):
#             tmp = dp.copy()
#             for u, v, price in flights:
#                 if dp[u] != float('inf') and dp[u] + price < tmp[v]:
#                     tmp[v] = dp[u] + price
#             dp = tmp      
#         return dp[dst] if dp[dst] != float('inf') else -1

import heapq
from collections import defaultdict, deque
from typing import List
# Djikstra solution:
# time complexity: O(E k log(Ek))
# space complexity: O(Ek)
class Solution:
    def findCheapestPrice(self,
                          n: int,
                          flights: list[list[int]],
                          src: int,
                          dst: int,
                          k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # min-heap entries are (cost_so_far, current_node, stops_used)
        heap = [(0, src, 0)]
        # best[(node, stops)] = lowest cost found to reach `node` using exactly `stops` stops
        best = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)
            # if we reach dst, this is the cheapest possible
            if node == dst:
                return cost
            # if still on the trip
            if stops <= k:
                for nei, price in adj[node]:
                    next_cost = cost + price
                    next_stops = stops + 1
                    # only accept if this is strictly better than any previous way
                    if next_cost < best.get((nei, next_stops), float('inf')):
                        best[(nei, next_stops)] = next_cost
                        heapq.heappush(heap, (next_cost, nei, next_stops))
        
        return -1