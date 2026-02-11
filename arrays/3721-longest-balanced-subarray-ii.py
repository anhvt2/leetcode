class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        # Segment tree node:
        # l, r   → range of prefix indices
        # mn, mx → min/max prefix balance in this range
        # lazy   → pending range increment
        class Node:
            __slots__ = ("l", "r", "mn", "mx", "lazy")
            def __init__(self):
                self.l = self.r = 0
                self.mn = self.mx = 0
                self.lazy = 0

        # Allocate segment tree (4x size is standard)
        tr = [Node() for _ in range((n + 1) * 4)]

        # Build tree over prefix index range [0, n]
        def build(u: int, l: int, r: int):
            tr[u].l, tr[u].r = l, r
            tr[u].mn = tr[u].mx = tr[u].lazy = 0  # initial balance = 0
            if l == r:
                return
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)

        # Apply range increment v to node u
        def apply(u: int, v: int):
            tr[u].mn += v
            tr[u].mx += v
            tr[u].lazy += v

        # Push lazy value to children
        def pushdown(u: int):
            if tr[u].lazy != 0:
                apply(u << 1, tr[u].lazy)
                apply(u << 1 | 1, tr[u].lazy)
                tr[u].lazy = 0

        # Recompute mn/mx from children
        def pushup(u: int):
            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn)
            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx)

        # Range add v to interval [l, r]
        # Used to update suffix prefix-balances
        def modify(u: int, l: int, r: int, v: int):
            if tr[u].l >= l and tr[u].r <= r:
                apply(u, v)
                return
            pushdown(u)
            mid = (tr[u].l + tr[u].r) >> 1
            if l <= mid:
                modify(u << 1, l, r, v)
            if r > mid:
                modify(u << 1 | 1, l, r, v)
            pushup(u)

        # Binary search in segment tree:
        # find smallest index whose prefix balance == target
        def query(u: int, target: int) -> int:
            if tr[u].l == tr[u].r:
                return tr[u].l
            pushdown(u)
            if tr[u << 1].mn <= target <= tr[u << 1].mx:
                return query(u << 1, target)
            return query(u << 1 | 1, target)

        build(1, 0, n)

        last = {}          # last occurrence of each number
        now = ans = 0      # now = current prefix balance

        for i, x in enumerate(nums, start=1):
            # det = +1 for odd, -1 for even
            det = 1 if (x & 1) else -1

            # If duplicate, remove previous contribution
            if x in last:
                modify(1, last[x], n, -det)  # subtract from suffix
                now -= det

            # Add new contribution at position i
            last[x] = i
            modify(1, i, n, det)             # add to suffix
            now += det

            # Find earliest prefix with same balance
            pos = query(1, now)

            # Update maximum balanced subarray length
            ans = max(ans, i - pos)

        return ans
