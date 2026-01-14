class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Precompute total area
        total = sum(l*l for _, _, l in squares)
        target = total / 2

        # Determine search range
        lo = min(y for _,y,_ in squares)
        hi = max(y+l for _,y,l in squares)

        def area_below(m: float) -> float:
            """
            Compute area below y=m counting overlap multiple times.
            """
            s = 0.0
            for x, y, l in squares:
                if m <= y:
                    continue
                cover = min(m - y, l)
                s += cover * l
            return s

        # Binary search to approximate the line
        for _ in range(60):
            mid = (lo + hi) / 2
            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid
        return lo
