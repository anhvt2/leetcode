class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        from math import isqrt, ceil
        from functools import reduce
        from operator import xor

        MOD = 10**9 + 7

        n = len(nums)
        threshold = isqrt(n)

        # group small-step queries by step value
        groups: list[list[tuple[int, int, int]]] = [[] for _ in range(threshold)]

        for left, right, step, value in queries:
            if step < threshold:
                groups[step].append((left, right, value))
            else:
                # large step: apply directly, few indices touched
                for idx in range(left, right + 1, step):
                    nums[idx] = nums[idx] * value % MOD

        diff = [1] * (n + threshold)

        for step in range(1, threshold):
            if not groups[step]:
                continue

            diff[:n + step] = [1] * (n + step)  # reset only needed slice

            for left, right, value in groups[step]:
                diff[left] = diff[left] * value % MOD
                stop = left + (ceil((right - left + 1) / step)) * step
                diff[stop] = diff[stop] * pow(value, MOD - 2, MOD) % MOD

            # prefix-product propagation along stride
            for idx in range(step, n):
                diff[idx] = diff[idx] * diff[idx - step] % MOD

            for idx in range(n):
                nums[idx] = nums[idx] * diff[idx] % MOD

        return reduce(xor, nums)