class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        if all(x == 0 for x in nums):
            return 0

        def ok(k: int) -> bool:
            diff = [0] * (n+1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r+1] -= val

            prefix = 0
            for i in range(n):
                prefix += diff[i]
                if prefix < nums[i]:
                    return False
            return True

        if not ok(len(queries)):
            return -1

        low, high = 0, len(queries)
        while low < high:
            mid = (low + high) // 2
            if ok(mid):
                high = mid
            else:
                low = mid + 1
        return low