from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # dp[i] = number of ways to partition first i elements (nums[0..i-1])
        # dp[0] = 1 (empty prefix)
        # We'll store prefix sums pref where pref[i] = (dp[0] + dp[1] + ... + dp[i]) % MOD
        # so that sum(dp[L..R]) = (pref[R] - pref[L-1]) % MOD
        pref = [0] * (n + 1)
        pref[0] = 1  # dp[0] = 1, so pref[0] = 1

        # Two monotonic deques storing indices of elements in the current window [l..i-1]:
        # - max_deque: indices in decreasing order of nums (front holds index of current max)
        # - min_deque: indices in increasing order of nums (front holds index of current min)
        max_deque = deque()
        min_deque = deque()

        l = 0  # left boundary of window; for current i window is nums[l..i-1]

        # process i from 1..n, where i corresponds to including element nums[i-1]
        for i in range(1, n + 1):
            x = nums[i - 1]

            # --- insert new element at index i-1 into monotonic deques ---
            # Maintain decreasing order in max_deque (remove smaller elements from the end)
            while max_deque and nums[max_deque[-1]] <= x:
                max_deque.pop()
            max_deque.append(i - 1)

            # Maintain increasing order in min_deque (remove larger elements from the end)
            while min_deque and nums[min_deque[-1]] >= x:
                min_deque.pop()
            min_deque.append(i - 1)

            # --- advance left boundary l while current window violates condition ---
            # window currently [l..i-1]. We want max - min <= k.
            # max = nums[max_deque[0]], min = nums[min_deque[0]]
            while l <= i - 1 and nums[max_deque[0]] - nums[min_deque[0]] > k:
                # If left index equals front of any deque, pop it because we're moving l forward
                if max_deque and max_deque[0] == l:
                    max_deque.popleft()
                if min_deque and min_deque[0] == l:
                    min_deque.popleft()
                l += 1

            # Now L = l is the smallest index so that nums[L..i-1] satisfies max-min <= k.
            # dp[i] = sum_{j=L..i-1} dp[j] = pref[i-1] - pref[L-1]
            left_pref_idx = l - 1  # pref index for L-1 (when L==0 we use pref[-1] semantics below)
            total = pref[i - 1]
            subtract = pref[left_pref_idx] if left_pref_idx >= 0 else 0
            dp_i = (total - subtract) % MOD

            # store dp_i into pref for future use: pref[i] = pref[i-1] + dp_i
            pref[i] = (pref[i - 1] + dp_i) % MOD

        # dp[n] = pref[n] - pref[n-1], but we can compute dp[n] directly:
        # dp[n] = (pref[n] - pref[n-1]) % MOD
        result = (pref[n] - pref[n - 1]) % MOD
        return result
