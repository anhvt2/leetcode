"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List, Optional

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        if n == 0:
            return None

        # Build 2D prefix sums: ps[i+1][j+1] = sum of grid[0..i][0..j]
        ps = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
                ps[i+1][j+1] = ps[i][j+1] + row_sum

        def sum_region(r0: int, c0: int, size: int) -> int:
            r1, c1 = r0 + size, c0 + size
            return ps[r1][c1] - ps[r0][c1] - ps[r1][c0] + ps[r0][c0]

        def build(r: int, c: int, size: int) -> 'Node':
            total = sum_region(r, c, size)
            if total == 0:                      # all zeros
                return Node(False, True, None, None, None, None)
            if total == size * size:            # all ones
                return Node(True, True, None, None, None, None)

            # Mixed region: split into four quadrants
            half = size // 2
            tl = build(r,         c,         half)
            tr = build(r,         c + half,  half)
            bl = build(r + half,  c,         half)
            br = build(r + half,  c + half,  half)

            # For internal nodes, 'val' is unused by the judge; set to True by convention
            return Node(True, False, tl, tr, bl, br)

        return build(0, 0, n)
