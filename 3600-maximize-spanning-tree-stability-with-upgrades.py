class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        # Idea:
        # Maximize the minimum edge strength in the spanning tree.
        # Use binary search on answer T (candidate stability).
        # For each T, check if we can build a spanning tree where every edge has effective strength ≥ T
        # using ≤ k upgrades. Use Union-Find to test connectivity and cycles.

        parent = list(range(n))

        def find(x):
            # Path-compressed find
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            # Union components; return False if cycle
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            parent[rb] = ra
            return True

        def feasible(T):
            # Check if a spanning tree with min edge strength ≥ T exists

            # Reset DSU
            for i in range(n):
                parent[i] = i

            upgrades = 0  # upgrades used
            used = 0      # edges in the tree so far

            optional = []

            # Step 1: force include mandatory edges
            for u, v, s, must in edges:
                if must:
                    # mandatory edges cannot be upgraded
                    if s < T:
                        return False
                    # cycle among mandatory edges invalidates spanning tree
                    if not union(u, v):
                        return False
                    used += 1
                else:
                    optional.append((u, v, s))

            # Step 2: classify optional edges by usability
            free_edges = []    # usable without upgrade
            need_upgrade = []  # usable only if upgraded

            for u, v, s in optional:
                if s >= T:
                    free_edges.append((u, v))
                elif s * 2 >= T:
                    need_upgrade.append((u, v))
                # else: unusable even with upgrade

            # Step 3: greedily connect components (Kruskal-style)
            # Prefer free edges first to minimize upgrades
            for u, v in free_edges:
                if union(u, v):
                    used += 1

            for u, v in need_upgrade:
                if union(u, v):
                    upgrades += 1
                    used += 1
                    if upgrades > k:
                        return False

            # Valid spanning tree must have exactly n-1 edges
            return used == n - 1

        # Binary search the maximum feasible stability
        lo, hi = 0, max(s * 2 for _, _, s, _ in edges)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid       # mid is feasible → try larger stability
                lo = mid + 1
            else:
                hi = mid - 1

        return ans