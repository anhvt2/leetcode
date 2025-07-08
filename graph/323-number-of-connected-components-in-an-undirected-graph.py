from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        # Step 2: DFS function
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        # Step 3: Count connected components
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        return components

