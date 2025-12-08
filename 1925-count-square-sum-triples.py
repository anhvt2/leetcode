class Solution:
    def countTriples(self, n: int) -> int:
        total = 0
        squares = set([i**2 for i in range(n+1)])

        for x in range(1, n+1):
            for y in range(x+1, n+1):
                if x**2 + y**2 in squares:
                    total += 2
        return total