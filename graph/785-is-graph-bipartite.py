from collections import deque
from typing import List

'''
Color each node with 0/1 so that adjacent nodes have opposite colors.
Run BFS from every uncolored node (the graph can be disconnected) to color nodes alternatively.
If we ever see an edge connecting same-colored nodes (or a self-loop), it's not bipartite.
'''

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0/1 are the two colors

        for start in range(n):
            if color[start] != -1:
                continue
            # BFS from this component
            color[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v == u:                 # self-loop => not bipartite
                        return False
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True