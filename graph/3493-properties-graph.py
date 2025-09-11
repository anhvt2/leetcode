class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        properties = [set(arr) for arr in properties] # Each row of properties is converted to a set, so we can easily compute intersections (&) and ignore duplicates.
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if len(properties[i] & properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)

        visted = ['F'] * n

        def dfs(node):
            visted[node] = 'T'
            for v in adj[node]:
                if visted[v] == 'F':
                    dfs(v)

        count = 0
        for i in range(n):
            if visted[i] == 'T':
                continue
            else:
                dfs(i)
                count += 1

        return count