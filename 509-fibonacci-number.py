class Solution:
    def fib(self, n: int) -> int:
        F = []
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            F.append(0)
            F.append(1)
            i = 1
            while i < n:
                i += 1
                F.append(F[-2] + F[-1])
            return F[-1]