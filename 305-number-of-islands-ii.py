from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        count = 0
        res = []
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                # Union by rank
                if rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                elif rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                count -= 1

        land = set()
        for r, c in positions:
            if (r, c) in land:
                res.append(count)
                continue
            land.add((r, c))
            idx = r * n + c
            parent[idx] = idx
            rank[idx] = 0
            count += 1

            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                nidx = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) in land:
                    union(idx, nidx)

            res.append(count)

        return res
