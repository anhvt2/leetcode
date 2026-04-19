        """
        Key idea:
        - n ≤ 1000, q ≤ 1000
        - Each query updates a *patterned subsequence*:
              idx = l, l+k, l+2k, ...
        - So we directly simulate each query efficiently.

        Optimization:
        - For each query, only touch affected indices.
        - Total work: O(n * q) worst-case, but acceptable.
        """

        MOD = 10**9 + 7
        n = len(nums)

        for l, r, k, v in queries:
            # iterate through arithmetic progression indices
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD

        # compute XOR of final array
        ans = 0
        for x in nums:
            ans ^= x

        return ans