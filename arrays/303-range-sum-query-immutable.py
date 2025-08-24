class NumArray:
    # # ---- First solution
    # def __init__(self, nums: List[int]):
    #     self.cum = [0]
    #     for x in nums:
    #         self.cum.append(self.cum[-1] + x)

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.cum[right+1] - self.cum[left]

    # ---- Second solution
    def __init__(self, nums: List[int]):
        self.cum = []
        for x in nums:
            self.cum.append(self.cum[-1] + x) if self.cum else self.cum.append(x)
    
    def sumRange(self, left:int, right: int) -> int:
        return self.cum[right] - self.cum[left-1] if left else self.cum[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)