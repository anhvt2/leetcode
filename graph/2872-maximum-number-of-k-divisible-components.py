from typing import List
import sys

# Increase recursion limit because the tree can be a long chain (depth = n)
sys.setrecursionlimit(10**7)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        n:     number of nodes
        edges: undirected tree edges
        values: value of each node
        k:     divisor requirement
        """

        # ------------------------------
        # Build adjacency list for graph
        # ------------------------------
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        # This stores the total number of components formed
        ans = 0

        # ------------------------------------------------------------------
        # DFS FUNCTION:
        # dfs(u, parent) returns the "subtree sum" rooted at node u.
        # If the subtree sum is divisible by k, then this subtree can become
        # one K-divisible component by cutting the edge above u.
        # ------------------------------------------------------------------
        def dfs(u: int, parent: int) -> int:
            nonlocal ans

            # Start subtree sum with the value of the current node
            subtree_sum = values[u]

            # Explore all neighbors (children) except the parent
            for v in g[u]:
                if v == parent:
                    # Don't go back up the tree
                    continue

                # Add child's subtree sum
                subtree_sum += dfs(v, u)

            # --------------------------------------------------------------
            # If this subtree is divisible by k,
            # then this subtree itself is a valid component.
            #
            # Even if we "cut" here, it does not affect other subtrees,
            # because these cuts are independent.
            # --------------------------------------------------------------
            if subtree_sum % k == 0:
                ans += 1  # one new component

            # Return this subtree's total sum
            return subtree_sum

        # Run DFS from node 0 (any node works, since it is a tree)
        dfs(0, -1)

        # ans already includes the whole-tree component if its sum % k == 0,
        # which matches the problem definition.
        return ans
