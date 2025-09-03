from typing import List
import sys
sys.setrecursionlimit(1 << 20)

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        tin = [0] * n
        tout = [0] * n
        sx = [0] * n
        time = 0

        def dfs(u: int, p: int) -> None:
            nonlocal time
            tin[u] = time
            time += 1
            sx[u] = nums[u]
            for v in g[u]:
                if v == p:
                    continue
                dfs(v, u)
                sx[u] ^= sx[v]
            tout[u] = time

        dfs(0, -1)
        total = sx[0]

        def is_ancestor(a: int, b: int) -> bool:
            # a is ancestor of b in the rooted tree
            return tin[a] <= tin[b] and tout[b] <= tout[a]

        ans = float('inf')
        # choose two cut edges (equivalently, two child nodes whose parent edges are cut)
        for i in range(1, n):
            for j in range(i + 1, n):
                if is_ancestor(i, j):
                    a = sx[j]
                    b = sx[i] ^ sx[j]
                    c = total ^ sx[i]
                elif is_ancestor(j, i):
                    a = sx[i]
                    b = sx[j] ^ sx[i]
                    c = total ^ sx[j]
                else:
                    a = sx[i]
                    b = sx[j]
                    c = total ^ sx[i] ^ sx[j]

                mxx = max(a, b, c)
                mnn = min(a, b, c)
                ans = min(ans, mxx - mnn)

        return ans
