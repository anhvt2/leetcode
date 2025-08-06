from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # Build a segment‐tree over baskets to support:
        #  - find_first(q): leftmost j with baskets[j] >= qs
        #  - mark j as used (set to -inf)
        n = len(baskets)
        size = 1
        while size < n:
            size <<= 1
        # tree[i] will store max capacity in that node's range
        tree = [-(10**18)] * (2 * size)
        # initialize leaves
        for i, cap in enumerate(baskets):
            tree[size + i] = cap
        # build upwards
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2*i], tree[2*i + 1])

        def find_first(q: int) -> int:
            """Return leftmost index j with baskets[j] >= q, or -1 if none."""
            if tree[1] < q:
                return -1
            idx, l, r = 1, 0, size - 1
            while idx < size:
                left = idx * 2
                mid = (l + r) // 2
                if tree[left] >= q:
                    idx, r = left, mid
                else:
                    idx, l = left + 1, mid + 1
            j = idx - size
            return j if j < n else -1

        def mark_used(j: int) -> None:
            """Mark basket j as used by setting its capacity to -inf."""
            pos = size + j
            tree[pos] = -(10**18)
            pos //= 2
            while pos:
                tree[pos] = max(tree[2*pos], tree[2*pos + 1])
                pos //= 2

        unplaced = 0
        # Place each fruit in the leftmost available basket >= its quantity
        for qty in fruits:
            j = find_first(qty)
            if j == -1:
                unplaced += 1
            else:
                mark_used(j)
        return unplaced
