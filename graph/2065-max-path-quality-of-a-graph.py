from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        # Number of nodes
        n = len(values)

        # ----------------------------
        # 1. Build an undirected graph
        # ----------------------------
        # g[u] = list of (v, time_cost)
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        # -------------------------------------------------------
        # 2. Precompute the shortest travel time from each node
        #    back to node 0 using Dijkstra’s algorithm.
        #    This helps prune DFS paths that can't return in time.
        # -------------------------------------------------------
        INF = 10**18
        dist0 = [INF] * n   # dist0[i] = shortest time from i → 0
        dist0[0] = 0
        pq = [(0, 0)]       # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist0[u]:   # Skip outdated entries
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist0[v]:
                    dist0[v] = nd
                    heapq.heappush(pq, (nd, v))

        # After this, dist0[v] holds the minimal time needed
        # to return from v to 0 (or INF if unreachable).

        # ---------------------------------------------------
        # 3. DFS traversal over all valid walks (backtracking)
        # ---------------------------------------------------
        best = 0                   # Global best path quality found
        visited = [0] * n          # Track how many times each node is visited

        def dfs(u: int, t: int, score: int) -> None:
            """
            Parameters:
                u     - current node
                t     - total time spent so far
                score - accumulated node values (unique nodes only)
            """
            nonlocal best

            # If we are currently at node 0, update the best score.
            # The path is valid because it ends at 0.
            if u == 0:
                best = max(best, score)

            # Explore neighbors
            for v, w in g[u]:
                nt = t + w  # time after moving u -> v

                # --- Pruning step ---
                # If we can't return from v to 0 within maxTime, skip it
                if nt + dist0[v] > maxTime:
                    continue

                # If first time visiting v, its value contributes to score
                added = 0
                if visited[v] == 0:
                    added = values[v]

                # Mark visit and recurse
                visited[v] += 1
                dfs(v, nt, score + added)
                visited[v] -= 1  # backtrack

        # Start DFS from node 0
        visited[0] = 1
        dfs(0, 0, values[0])

        # Return the maximum path quality achievable
        return best
