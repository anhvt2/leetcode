from collections import deque
from typing import List

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if n <= 1:
            return 0

        g = [[] for _ in range(n)]
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # 1) Prune leaves with no coins
        q = deque(i for i in range(n) if deg[i] == 1 and coins[i] == 0)
        while q:
            u = q.popleft()
            if deg[u] == 0:
                continue
            deg[u] = 0
            for v in g[u]:
                if deg[v] > 0:
                    deg[v] -= 1
                    if deg[v] == 1 and coins[v] == 0:
                        q.append(v)

        # 2) Trim two layers of coin leaves
        dist = [-1] * n
        q = deque(i for i in range(n) if deg[i] == 1 and coins[i] == 1)
        for i in list(q):
            dist[i] = 0
        while q:
            u = q.popleft()
            if dist[u] >= 2:
                continue
            for v in g[u]:
                if deg[v] > 0:
                    deg[v] -= 1
                    if deg[v] == 1 and dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            deg[u] = 0

        # 3) Remaining edges and total steps
        return sum(deg)
