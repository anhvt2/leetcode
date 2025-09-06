from typing import List
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def f(x: int) -> int:
            # total "individual picks" needed for all numbers in [1..x]
            if x <= 0:
                return 0
            res = 0
            p = 1   # 4^(i-1)
            i = 1   # level index
            while p <= x:
                # count how many numbers of [p .. min(4*p-1, x)] fall in this level
                cnt = min(p * 4 - 1, x) - p + 1
                res += cnt * i
                i += 1
                p *= 4
            return res

        ans = 0
        for l, r in queries:
            s = f(r) - f(l - 1)     # sum of individual needs in [l..r]
            mx = f(r) - f(r - 1)    # max individual need in [l..r], achieved at r
            ans += max((s + 1) // 2, mx)
        return ans
