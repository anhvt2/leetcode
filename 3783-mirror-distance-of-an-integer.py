class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            return int(str(n)[::-1])
        return abs(n - reverse(n))