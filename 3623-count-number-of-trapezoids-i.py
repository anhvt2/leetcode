from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7

        # ------------------------------------------------------------
        # 1. Group points by their y-coordinate.
        #    Each y-level can produce horizontal edges.
        # ------------------------------------------------------------
        groups = defaultdict(int)
        for x, y in points:
            groups[y] += 1   # count how many points lie on each horizontal line y

        # ------------------------------------------------------------
        # 2. For each y-level with m points:
        #       number of horizontal segments = C(m, 2) = m*(m-1)/2
        #    Store these values in array a.
        # ------------------------------------------------------------
        a = []
        for count in groups.values():
            if count >= 2:
                # Number of unordered horizontal edges on this y-level
                a.append(count * (count - 1) // 2)

        # ------------------------------------------------------------
        # 3. Let a = [e1, e2, e3, ...]
        #
        # Total trapezoids = sum over all unordered pairs of i < j of (ei * ej).
        #
        # Notice a combinatorics identity:
        #     (e1 + e2 + e3 + ...)^2
        #       = e1^2 + e2^2 + e3^2 + ...        (self-pairs)
        #         + 2 * (e1*e2 + e1*e3 + e2*e3 + ...)
        #
        # Let:
        #     S = sum(ei)
        #     T = sum(ei^2)
        #
        # Then:
        #     S^2 - T = 2 * sum(ei * ej for i < j)
        #
        # So the number of trapezoids = (S^2 - T) / 2.
        # ------------------------------------------------------------
        S = sum(a)                    # S = sum(ei)
        T = sum(x * x for x in a)     # T = sum(ei^2)

        # ------------------------------------------------------------
        # 4. Final result modulo 1e9+7.
        # ------------------------------------------------------------
        return (S * S - T) // 2 % mod
