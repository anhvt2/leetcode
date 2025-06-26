class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        tmp = []
        for k, v in Counter(nums).items():
            if v == 1:
                tmp.append(k)
        return sum(tmp)