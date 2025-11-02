class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """

        # time: O(n), space: O(1)
        # sliding window, at most one zero: keep a window [l..r] that contains <= 1 zero. Expand `r` if window has >1 zeros, move `l` right until it has <=1 zero again. Track the longest window length
        l = 0
        zero_count = 0
        best = 0

        for r, num in enumerate(nums):
            if num == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1

                l += 1

            best = max(best, r - l + 1)
        return best