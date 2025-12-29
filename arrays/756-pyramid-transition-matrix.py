from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        Algorithm:
        ----------
        1. Convert allowed transitions into a map:
           (char1, char2) -> list of possible upper chars.
        2. Use DFS to attempt building the pyramid from bottom to top.
        3. Memoize failed rows to prune the search space.

        Time Complexity: Exponential in worst case, but heavily pruned.
        Space Complexity: O(states) for memoization.
        """

        # Build transition map
        trans = defaultdict(list)
        for a in allowed:
            trans[(a[0], a[1])].append(a[2])

        # Memoization set for failed states
        bad = set()

        def dfs(row: str) -> bool:
            # Base case: reached the top
            if len(row) == 1:
                return True

            if row in bad:
                return False

            # Build next row via backtracking
            def build_next(i: int, cur: List[str]) -> bool:
                if i == len(row) - 1:
                    # Recurse to next level
                    return dfs("".join(cur))

                pair = (row[i], row[i + 1])
                if pair not in trans:
                    return False

                for c in trans[pair]:
                    cur.append(c)
                    if build_next(i + 1, cur):
                        return True
                    cur.pop()

                return False

            if not build_next(0, []):
                bad.add(row)
                return False

            return True

        return dfs(bottom)
