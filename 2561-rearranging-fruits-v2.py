from typing import List, Tuple
from collections import defaultdict

def balance_sums(
    b1: List[int], 
    b2: List[int]
) -> Tuple[List[int], List[int]]:
    sum1, sum2 = sum(b1), sum(b2)
    diff = sum1 - sum2
    # If diff is odd, no single‐swap solution exists
    if diff % 2 != 0:
        return b1, b2

    # We need a - b = diff//2
    target = diff // 2

    # Build a map from value in b2 to its indices
    pos2 = defaultdict(list)
    for j, val in enumerate(b2):
        pos2[val].append(j)

    # Find the first a in b1 such that (a - target) exists in b2
    for i, a in enumerate(b1):
        b = a - target
        if pos2[b]:
            j = pos2[b][0]
            # swap
            b1[i], b2[j] = b2[j], b1[i]
            return b1, b2

    # no single‐swap solution found
    return b1, b2


# Example
basket1 = [4,2,2,2]
basket2 = [1,4,1,2]
b1_bal, b2_bal = balance_sums(basket1, basket2)
print(b1_bal)  # [4, 1, 2, 2]
print(b2_bal)  # [2, 4, 1, 2]
