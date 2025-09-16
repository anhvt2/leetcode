from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for x in nums:
            cur = x
            # keep merging with previous while not coprime
            while st:
                g = gcd(st[-1], cur)
                if g == 1:
                    break
                # merge last and cur into their LCM
                cur = st[-1] // g * cur
                st.pop()
            st.append(cur)
        return st
