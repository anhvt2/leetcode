
from typing import List
from collections import defaultdict, deque
import bisect

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        # build rooted tree (children lists)
        children = [[] for _ in range(n)]
        root = 0
        for u in range(1, n):
            p = par[u]
            children[p].append(u)

        # 1) path XOR from root to each node
        px = vals[:]  # will become XOR(root->u)
        def dfs_xor(u: int) -> None:
            for v in children[u]:
                px[v] ^= px[u]
                dfs_xor(v)
        dfs_xor(root)

        # attach queries to their node
        qs = defaultdict(list)   # node -> list[(k, idx)]
        for idx, (u, k) in enumerate(queries):
            qs[u].append((k, idx))

        ans = [-1] * len(queries)

        # 2) DSU on tree: return sorted unique px-values list for subtree
        def dfs(u: int) -> List[int]:
            # start with this node's px
            cur = [px[u]]

            for v in children[u]:
                lst = dfs(v)  # child's list
                # small-to-large: merge smaller into larger
                if len(lst) > len(cur):
                    cur, lst = lst, cur
                # merge 'lst' into 'cur' keeping distinct and sorted
                for x in lst:
                    i = bisect.bisect_left(cur, x)
                    if i == len(cur) or cur[i] != x:
                        cur.insert(i, x)

            # answer queries on u
            if u in qs:
                for k, idx in qs[u]:
                    if k <= len(cur):
                        ans[idx] = cur[k - 1]
                    else:
                        ans[idx] = -1
            return cur

        dfs(root)
        return ans
