from typing import List
from collections import defaultdict
import heapq

class Solution:
    # -------------------------------
    # Inner class: Disjoint Set Union (Union-Find)
    # -------------------------------
    class DSU:
        def __init__(self, n: int):
            # Each node is initially its own parent (self.p[i] = i)
            self.p = list(range(n + 1))
            # "Rank" array for union by rank optimization
            self.r = [0] * (n + 1)

        def find(self, x: int) -> int:
            """Return the representative (root) of the set containing x."""
            # Path compression: flatten the tree for efficiency
            while self.p[x] != x:
                self.p[x] = self.p[self.p[x]]
                x = self.p[x]
            return x

        def union(self, a: int, b: int) -> None:
            """Merge the sets that contain a and b."""
            ra, rb = self.find(a), self.find(b)
            if ra == rb:
                return  # already in same set
            # Union by rank: attach smaller tree to larger one
            if self.r[ra] < self.r[rb]:
                ra, rb = rb, ra
            self.p[rb] = ra
            if self.r[ra] == self.r[rb]:
                self.r[ra] += 1

    # -----------------------------------
    # Main function to process the queries
    # -----------------------------------
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Build static connectivity using DSU
        dsu = self.DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        # Step 2: Create a min-heap of station IDs per component
        # Each component (identified by DSU root) has a heap of its station IDs
        comp_heap = defaultdict(list)
        for node in range(1, c + 1):
            root = dsu.find(node)
            comp_heap[root].append(node)
        for comp in comp_heap:
            heapq.heapify(comp_heap[comp])  # turn lists into heaps (min-heaps)

        # Step 3: Track online/offline status (all stations start online)
        online = [False] + [True] * c  # 1-based indexing (ignore index 0)

        # Step 4: Process queries
        ans = []
        for t, x in queries:
            if t == 2:
                # Type 2: Station x goes offline
                online[x] = False

            else:  # t == 1 → maintenance check
                if online[x]:
                    # If x is online, it resolves itself
                    ans.append(x)
                else:
                    # Otherwise, find smallest online station in same component
                    comp = dsu.find(x)
                    h = comp_heap[comp]
                    # Lazy deletion: pop offline stations from heap top
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    # Append smallest available online station or -1 if none
                    ans.append(h[0] if h else -1)

        return ans
