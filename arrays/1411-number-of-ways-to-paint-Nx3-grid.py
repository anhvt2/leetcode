class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Algorithm:
        ----------
        Use dynamic programming with two states per row:

        - aba: number of ways to paint the current row using an ABA pattern
               (first and third same, middle different)
        - abc: number of ways to paint the current row using an ABC pattern
               (all three colors different)

        Initialization (row 1):
        - aba = 6
        - abc = 6

        Transitions:
        - new_abc = 2 * abc + 2 * aba
        - new_aba = 2 * abc + 3 * aba

        Iterate row-by-row and update the states.
        The answer is (aba + abc) % MOD.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        MOD = 10**9 + 7

        aba = 6
        abc = 6

        for _ in range(2, n + 1):
            new_abc = (2 * abc + 2 * aba) % MOD
            new_aba = (2 * abc + 3 * aba) % MOD
            abc, aba = new_abc, new_aba

        return (abc + aba) % MOD
