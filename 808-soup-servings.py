from functools import lru_cache
import math

class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0  # approximation cutoff

        N = math.ceil(n / 25)

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5  # both finish
            if a <= 0:
                return 1.0  # A first
            if b <= 0:
                return 0.0  # B first

            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(N, N)
