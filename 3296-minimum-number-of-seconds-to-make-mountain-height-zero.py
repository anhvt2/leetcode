class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Idea:
        # Binary search the minimum time T such that workers can collectively reduce ≥ mountainHeight.
        #
        # For worker with time w:
        # Reducing x height takes:
        #   w*(1 + 2 + ... + x) = w * x*(x+1)/2
        #
        # Given time T, the worker can do maximum x satisfying:
        #   w * x*(x+1)/2 ≤ T
        #
        # Solve quadratic:
        #   x^2 + x - (2T/w) ≤ 0
        #
        # Largest integer x:
        #   x = floor((sqrt(1 + 8T/w) - 1) / 2)

        import math

        def can(T):
            total = 0
            for w in workerTimes:
                # max height this worker can reduce within T
                x = int((math.sqrt(1 + 8*T//w) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False

        lo, hi = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo