from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Split nums1 into negative and non-negative parts
        neg = [e for e in nums1 if e < 0]
        pos = [e for e in nums1 if e >= 0]

        # Create reversed versions (to process in different orders later)
        negRev = neg[::-1]   # reverse negatives (from closest to zero to most negative)
        posRev = pos[::-1]   # reverse positives (largest to smallest)

        # Helper function: count how many products <= val
        def fn(val: int) -> int:
            res = 0                  # number of pairs with product <= val
            n = len(nums2)           # length of second array
            l, r = 0, n - 1          # two pointers for scanning nums2

            # The order of processing depends on the sign of val:
            # If val >= 0: use negRev + pos
            # If val < 0:  use neg + posRev
            if val >= 0:
                lst = negRev + pos
            else:
                lst = neg + posRev

            # For each element e in nums1 (arranged by lst):
            for e in lst:
                if e < 0:
                    # For negative e:
                    # Move pointer l forward until e * nums2[l] <= val
                    while l < n and e * nums2[l] > val:
                        l += 1
                    # All remaining nums2[l..n-1] form valid products
                    res += n - l

                elif e == 0:
                    # For zero: product is 0, valid only if val >= 0
                    if val >= 0:
                        res += n

                else:  # e > 0
                    # For positive e:
                    # Move pointer r backward until e * nums2[r] <= val
                    while r >= 0 and e * nums2[r] > val:
                        r -= 1
                    # All nums2[0..r] form valid products
                    res += r + 1
            return res

        # Binary search over possible product values
        l, r = -(10 ** 10), 10 ** 10  # wide enough search range
        while l < r:
            mid = l + (r - l) // 2    # candidate product value
            if fn(mid) < k:
                # Not enough products <= mid → need larger values
                l = mid + 1
            else:
                # Enough products <= mid → mid could be the answer
                r = mid
        return l   # left bound is the k-th smallest product
