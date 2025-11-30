from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        Return the minimum length of a contiguous subarray that we can remove
        so that the sum of the remaining elements is divisible by p.
        If impossible, return -1.
        """

        # Total sum modulo p: the remainder we need to remove from the array.
        total_mod = sum(nums) % p
        # If total_mod is 0, the whole array sum is already divisible by p.
        if total_mod == 0:
            return 0

        # Map: prefix_mod -> latest index where this prefix_mod occurred.
        # Initialize with prefix_mod 0 at index -1 (empty prefix).
        last_index = {0: -1}

        best = len(nums)  # store length of shortest subarray found; start with n (impossible sentinel)
        cur = 0           # current prefix sum modulo p

        # Walk through array, building prefix modulo and checking candidates
        for i, val in enumerate(nums):
            # update prefix modulo with current value
            cur = (cur + val) % p

            # We want pref[j] such that (cur - pref[j]) % p == total_mod
            # Rearranged: pref[j] % p == (cur - total_mod) % p
            need = (cur - total_mod) % p

            # If we've seen 'need' before at some index j, then
            # subarray (j+1 .. i) has sum % p == total_mod and can be removed.
            if need in last_index:
                j = last_index[need]
                length = i - j
                # update best (take the shorter)
                if length < best:
                    best = length

            # Record the latest index where this prefix modulo occurred.
            # We keep the latest index to maximize chance of shorter future subarray.
            last_index[cur] = i

        # If best was not updated (still n), it's impossible
        return best if best < len(nums) else -1
