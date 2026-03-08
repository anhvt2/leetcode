import random
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        def gen(n):
            trial = ""
            for _ in range(n):
                trial += str(random.choices([0,1])[0])
            return trial
        trial = gen(n)
        while trial in nums:
            trial = gen(n)
        return trial