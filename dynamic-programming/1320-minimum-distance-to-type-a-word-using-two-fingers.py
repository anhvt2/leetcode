class Solution:
    def minimumDistance(self, word: str) -> int:
        """
        Key idea:
        - Treat the keyboard as a grid:
            A(0,0), B(0,1), ..., Z(5,0)
        - We use DP where:
            dp[i][f][s] = minimum cost after typing first i characters,
                          with finger1 at f, finger2 at s
        - But full 3D DP is too large. Optimize:
            Fix one finger as "active", track the other as a variable.

        Better formulation:
        - Let dp[j] = max saved distance if the "free finger" is at letter j
        - We iterate through word, and greedily compute the benefit of using
          the second finger instead of always moving the first.

        Final answer = total distance using one finger - max saved distance
        """

        def dist(a, b):
            """Manhattan distance on keyboard"""
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        # Convert chars to indices 0-25
        w = [ord(c) - ord('A') for c in word]

        n = len(w)
        if n <= 2:
            return 0

        # total distance if we use only one finger
        total = 0
        for i in range(1, n):
            total += dist(w[i - 1], w[i])

        # dp[j] = max saving if second finger is currently at letter j
        dp = [0] * 26

        max_save = 0

        for i in range(1, n):
            cur = w[i]
            prev = w[i - 1]

            new_dp = dp[:]  # copy for updates

            for j in range(26):
                # Option: move second finger from j -> cur
                # saving = distance(prev, cur) - distance(j, cur)
                gain = dist(prev, cur) - dist(j, cur)
                new_dp[prev] = max(new_dp[prev], dp[j] + gain)

                max_save = max(max_save, new_dp[prev])

            dp = new_dp

        return total - max_save