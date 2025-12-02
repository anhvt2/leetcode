from collections import Counter
from itertools import combinations
from math import gcd, comb
from typing import List

class Solution:
    def countTrapezoids(self, A: List[List[int]]) -> int:
        """
        Count number of trapezoids (convex quadrilaterals with at least one pair
        of parallel sides) formed by choosing any 4 distinct points from A.

        The approach enumerates all unordered point-pairs (segments) and uses four
        histograms (Counters) to keep track of:
          - slopes:        how many segments have a given slope (direction)
          - lines:         how many segments lie on the exact same geometric line
          - mids:          how many segments share the same midpoint (twice the midpoint)
          - midlines:      how many segments share both midpoint and lie on the same line

        Then a short inclusion–exclusion combining these histograms yields the count.
        """

        # Count segments by slope (normalized direction)
        slopes = Counter()
        # Count segments by exact geometric line (slope + line constant)
        lines = Counter()
        # Count segments by midpoint (we store twice the midpoint, (x1+x2, y1+y2), to stay integer)
        mids = Counter()
        # Count segments by (midpoint + line) to correct double-counts in inclusion-exclusion
        midlines = Counter()

        # For each unordered pair of distinct points produce one segment
        # (combinations(A, 2) yields each unordered pair exactly once)
        for (x1, y1), (x2, y2) in combinations(A, 2):
            # raw direction vector from point1 to point2
            dx, dy = x2 - x1, y2 - y1

            # normalize the direction so (dx,dy) and (-dx,-dy) map to the same slope,
            # and reduce by gcd to avoid proportional duplicates (use integer slope).
            # gcd could be 0 only if dx == dy == 0 (identical points), but input gives
            # distinct points for combinations so gcd > 0 here.
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g

            # canonicalize sign: ensure dx > 0, or if dx == 0 then dy > 0.
            # This makes the slope representation unique (no double counting of opposite directions).
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            # "inter" is the line invariant (constant) for the normalized direction:
            # for a line parameterized by direction (dx,dy), the quantity (dx * y - dy * x)
            # is the same for all points (x,y) on that geometric line. Using that avoids floats.
            inter = dx * y1 - dy * x1

            # increment histogram entries:
            # - segments with the same slope (dx,dy)
            slopes[dx, dy] += 1
            # - segments on the exact same geometric line (dx,dy,inter)
            lines[dx, dy, inter] += 1
            # - segments sharing the same midpoint (store (x1+x2, y1+y2) to avoid fractions)
            mids[x1 + x2, y1 + y2] += 1
            # - segments that both share the midpoint and lie on the same line
            #   (used to correct over-subtraction)
            midlines[x1 + x2, y1 + y2, dx, dy, inter] += 1

        # -----------------------
        # Combinatorics explanation
        # -----------------------
        # Let:
        #  - slopes[(dx,dy)] = number of segments with that slope,
        #  - lines[...]        = number of segments on that exact line,
        #  - mids[...]         = number of segments with that midpoint,
        #  - midlines[...]     = number of segments with that midpoint on that line.
        #
        # 1) Total pairs of segments that have the same slope (including those on same line):
        #      sum_{slope} C(slopes[slope], 2)
        #    This counts every unordered pair of segments that are parallel, regardless of
        #    whether they lie on the same geometric line or not.
        #
        # 2) But segments that lie on the *same* line should not be counted as two bases of a
        #    trapezoid (they are collinear). Subtract the pairs that come from the same line:
        #      - sum_{line} C(lines[line], 2)
        #
        # 3) Among remaining pairs of parallel segments on different lines, pairs that are
        #    diagonals (i.e., pairs of point-pairs sharing the same midpoint) correspond to
        #    parallelograms; each parallelogram should *not* be counted as a trapezoid here
        #    (parallelograms have been included in the slope-based count but need separate
        #    treatment). So subtract pairs of segments that have exactly the same midpoint:
        #      - sum_{mid} C(mids[mid], 2)
        #
        # 4) The previous two subtractions (lines and mids) may have double–subtracted pairs
        #    that both lie on the same line *and* share the same midpoint (degenerate case:
        #    two identical segments counted twice); add them back:
        #      + sum_{midline} C(midlines[midline], 2)
        #
        # Putting these four inclusion/exclusion terms together gives the final count of
        # unordered pairs of segments that are parallel, lie on different lines, and do not
        # share midpoint — i.e., they form the two parallel bases of a trapezoid.
        #
        # The exact expression implemented below is:
        #    ans = sum(C(slopes)) - sum(C(lines)) - sum(C(mids)) + sum(C(midlines))

        # sum of C(v,2) for all slope groups
        ans = sum(comb(v, 2) for v in slopes.values())
        # subtract pairs that lie on the exact same line (collinear segments)
        ans -= sum(comb(v, 2) for v in lines.values())
        # subtract pairs that share the same midpoint (parallelogram diagonals --> parallelograms)
        ans -= sum(comb(v, 2) for v in mids.values())
        # add back those that were subtracted twice (same line & same midpoint)
        ans += sum(comb(v, 2) for v in midlines.values())

        return ans
