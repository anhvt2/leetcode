from collections import Counter
from typing import List
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        f1, f2 = Counter(basket1), Counter(basket2)
        # (1) global minimum fruit cost
        m = min(min(basket1), min(basket2))

        swaps = []
        # (2) check parity and build swap list
        for c in set(f1) | set(f2):
            total = f1[c] + f2[c]
            if total % 2 == 1:
                return -1
            need = f1[c] - (total // 2)
            # collect |need| fruits of cost c that must move
            swaps.extend([c] * abs(need))

        # (3) compute number of actual swaps
        swaps_needed = len(swaps) // 2
        swaps.sort()

        # (4) choose the cheaper of direct swap (cost c) or relay via min fruit (cost 2m)
        ans = 0
        for i in range(swaps_needed):
            ans += min(swaps[i], 2*m)

        return ans
        