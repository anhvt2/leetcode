from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # (1) Initialize the graph
        #    - adj[c] = set of characters that come directly after c
        #    - indegree[c] = number of edges coming into c
        adj = defaultdict(set)
        indegree = {}
        for w in words:
            for c in w:
                indegree.setdefault(c, 0)

        # (2) Build edges by comparing adjacent words
        for w1, w2 in zip(words, words[1:]):
            # invalid case: longer word appears before its own prefix
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            # find first mismatch and create an ordering edge
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break

        # (3) Collect all nodes with indegree 0
        queue = deque([c for c, d in indegree.items() if d == 0])
        order = []

        # (4) Kahn's algorithm
        while queue:
            c = queue.popleft()
            order.append(c)
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        # (5) If we were able to order every character, return it
        if len(order) == len(indegree):
            return "".join(order)
        # otherwise there’s a cycle → no valid ordering
        return ""
        