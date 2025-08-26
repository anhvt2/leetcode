from typing import List
MOD = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # 1) Generate all valid column states (each is a tuple of length m with values in {0,1,2})
        states = []
        def gen(col, prev):
            if len(col) == m:
                states.append(tuple(col))
                return
            for c in range(3):
                if c != prev:
                    col.append(c)
                    gen(col, c)
                    col.pop()
        gen([], -1)

        S = len(states)

        # 2) Build adjacency: columns must differ at every row
        compat = [[] for _ in range(S)]
        for i in range(S):
            a = states[i]
            for j in range(S):
                b = states[j]
                # adjacent columns cannot have same color in any row
                ok = True
                for r in range(m):
                    if a[r] == b[r]:
                        ok = False
                        break
                if ok:
                    compat[i].append(j)

        # 3) DP over columns
        dp = [1] * S  # first column: any valid state
        for _ in range(1, n):
            new = [0] * S
            for i in range(S):
                ways = dp[i]
                if ways:
                    for j in compat[i]:
                        new[j] = (new[j] + ways) % MOD
            dp = new

        return sum(dp) % MOD
