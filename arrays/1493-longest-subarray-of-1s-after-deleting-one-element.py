from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # ---- First solution
        # decompose nums into list of lists, convert non-1 to 0
        l = []
        tmp0, tmp1 = [], []
        has_zero = False
        for i, num in enumerate(nums):
            if num == 1:
                if tmp0: 
                    l.append(tmp0)
                    tmp0 = [] # reset
                tmp1.append(num)
            else: # num == 0
                has_zero = True
                if tmp1:
                    l.append(tmp1)
                    tmp1 = [] # reset
                tmp0.append(0)
        if tmp0: l.append(tmp0)
        if tmp1: l.append(tmp1)

        if not has_zero:
            return(len(nums) - 1)

        max1 = 0 # initialize
        for i in range(len(l)):
            if l[i][0] == 1:
                max1 = max(max1, len(l[i]))
                # if patterns ... [1s], [0s], [1s] ... we can bridge
                if (i + 2 < len(l) and len(l[i+1]) == 1):
                    max1 = max(max1, len(l[i] + l[i+2]))
        return max1

        # ---- Second solution
        # left = 0
        # zeros = 0
        # best = 0

        # for right, x in enumerate(nums):
        #     if x == 0:
        #         zeros += 1
        #     # move left pointers until the last zero
        #     while zeros > 1:
        #         if nums[left] == 0:
        #             zeros -= 1
        #         left += 1
        #     # delete one element (the single zero if present), so use right - left
        #     best = max(best, right - left)

        # return best

