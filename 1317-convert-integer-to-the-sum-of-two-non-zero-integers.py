from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def ok(x: int) -> bool:
            return x > 0 and '0' not in str(x)   # positive + no zero digit
        for a in range(1, n):                    # ensures a>=1 and b>=1
            b = n - a
            if ok(a) and ok(b):
                return [a, b]
