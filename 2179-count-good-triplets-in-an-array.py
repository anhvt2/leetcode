from typing import List

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.ft = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.ft[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.ft[i]
            i -= i & -i
        return s

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # map value -> index in nums2 (0-based)
        where = {v: i for i, v in enumerate(nums2)}
        # pos array (0-based), then shift by +1 for BIT convenience
        pos = [where[v] + 1 for v in nums1]

        # L[j]: count of smaller to the left
        bit = BIT(n)
        L = [0] * n
        for j in range(n):
            L[j] = bit.sum(pos[j] - 1)
            bit.add(pos[j], 1)

        # R[j]: count of greater to the right
        bit = BIT(n)
        R = [0] * n
        for j in range(n - 1, -1, -1):
            # elements to right already added; greater than pos[j]:
            R[j] = bit.sum(n) - bit.sum(pos[j])
            bit.add(pos[j], 1)

        # sum over j
        ans = 0
        for j in range(n):
            ans += L[j] * R[j]
        return ans
