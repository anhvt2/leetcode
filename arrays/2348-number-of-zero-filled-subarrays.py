class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_arrs = []
        tmp = []
        for i, num in enumerate(nums):
            if num == 0:
                tmp.append(num)
            if num != 0 and tmp:
                zero_arrs.append(tmp)
                tmp = [] # reset
        zero_arrs.append(tmp)
        count = 0
        for i, arr in enumerate(zero_arrs):
            n = len(arr)
            count += n * (n+1) // 2
        return count