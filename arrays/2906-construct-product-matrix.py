from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Idea:
        # - For each cell, want product of all other elements mod 12345
        # - Classic "product except self" WITHOUT division
        # - Flatten grid -> build prefix and suffix products
        # - prefix[i] = product of all before i
        #   suffix[i] = product of all after i
        # - answer[i] = prefix[i] * suffix[i] % MOD

        MOD = 12345
        m, n = len(grid), len(grid[0])

        # Flatten grid
        arr = [grid[i][j] for i in range(m) for j in range(n)]
        k = len(arr)

        # Build prefix products
        prefix = [1] * k
        for i in range(1, k):
            prefix[i] = prefix[i-1] * arr[i-1] % MOD

        # Build suffix products
        suffix = [1] * k
        for i in range(k-2, -1, -1):
            suffix[i] = suffix[i+1] * arr[i+1] % MOD

        # Combine prefix & suffix to get result
        res = [[0]*n for _ in range(m)]
        for idx in range(k):
            val = prefix[idx] * suffix[idx] % MOD
            i, j = divmod(idx, n)
            res[i][j] = val

        return res
