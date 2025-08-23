from typing import List, Optional

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # build adjacency list
        g = [[] for _ in range(n)]
        for a, b in roads:
            g[a].append(b)
            g[b].append(a)

        m = len(targetPath)
        INF = 10**9

        # dp[i][u]: min edits up to i if path[i] = u
        dp = [[INF] * n for _ in range(m)]
        parent = [[-1] * n for _ in range(m)]

        # init
        for u in range(n):
            dp[0][u] = 0 if names[u] == targetPath[0] else 1

        # transitions
        for i in range(1, m):
            for u in range(n):  # <-- include 0
                mismatch = 0 if names[u] == targetPath[i] else 1  # <-- use i
                best_prev = INF
                best_v = -1
                for v in g[u]:
                    if dp[i-1][v] < best_prev:
                        best_prev = dp[i-1][v]
                        best_v = v
                if best_v != -1:
                    dp[i][u] = mismatch + best_prev
                    parent[i][u] = best_v

        # choose best end
        end = min(range(n), key=lambda u: dp[m-1][u])

        # reconstruct path
        path = [end]
        for i in range(m-1, 0, -1):
            path.append(parent[i][path[-1]])
        path.reverse()          # <-- reverse in place
        return path
