from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        """
        Return the number of valid unlocking permutations modulo 1e9+7.
        """
        MOD = 10**9 + 7
        n = len(complexity)

        # If first computer's complexity is NOT strictly smaller than every
        # other computer's complexity, no full unlocking sequence exists.
        first = complexity[0]
        for i in range(1, n):
            if first >= complexity[i]:
                return 0

        # Otherwise the answer is (n-1)! modulo MOD.
        # Compute factorial iteratively to avoid large intermediate integers.
        res = 1
        for k in range(2, n):  # multiply from 2..n-1 (0! and 1! are 1)
            res = (res * k) % MOD
        return res
