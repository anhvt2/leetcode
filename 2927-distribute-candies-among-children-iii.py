class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Returns number of non-negative integer solutions to:
        # a + b + c = n (unbounded)
        def f(n):
            return 0 if n < 0 else (n + 1) * (n + 2) // 2  # C(n+2, 2)

        # Inclusion-Exclusion to enforce 0 ≤ a, b, c ≤ limit:
        # - Start with all unrestricted triplets: f(n)
        # - Subtract cases where one variable > limit
        # - Add back over-subtracted cases where two > limit
        # - Subtract triple-overcount where all three > limit
        L = limit + 1
        return f(n) - 3 * f(n - L) + 3 * f(n - 2 * L) - f(n - 3 * L)
