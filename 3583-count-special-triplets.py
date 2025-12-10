import math
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        hashmap = {}            # maps value -> list of indices where that value appears
        n = len(nums)

        # Build index lists for each value. Indices are appended in increasing order (0..n-1),
        # so each list in hashmap[value] is sorted ascending.
        for i in range(n):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = []
            hashmap[nums[i]].append(i)

        res = 0

        # For each distinct value 'el' that can serve as the "double" (i.e. el == 2 * nums[j])
        for el, double in hashmap.items():
            # Case 1: el == 0. Then 0 == 2 * 0, so any triple of indices among zeros
            # with i < j < k is valid. Count them with C(m, 3).
            if el == 0:
                m = len(double)             # number of zeros
                if m >= 3:
                    res += math.comb(m, 3)
                continue

            # Case 2: el != 0.
            # Only possible if el is even (so el//2 is an integer and could be present).
            if el % 2 == 0 and (el // 2) in hashmap:
                # 'double' is the list of indices where value == el (these are candidates for i and k)
                # 'single' is the list of indices where value == el//2 (these are candidates for j)
                single = hashmap[el // 2]

                # We will count, for each j in single, how many 'double' indices are strictly left of j
                # and strictly right of j. The product is the number of (i,k) choices for that j.
                # 'double' and 'single' are both sorted ascending.
                i_ptr = 0
                len_double = len(double)
                for s in single:
                    # advance i_ptr until double[i_ptr] >= s (i_ptr counts indices < s)
                    while i_ptr < len_double and double[i_ptr] < s:
                        i_ptr += 1
                    # now i_ptr == number of double indices strictly less than s
                    left_count = i_ptr
                    right_count = len_double - i_ptr   # number of double indices strictly greater than s
                    # accumulate product
                    res += left_count * right_count

        return res % MOD
