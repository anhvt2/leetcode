class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            target = num1 - num2 * i # 'target' must equal the sum of exactly i powers of two (with repetition allowed)
            if target >= 0 and bin(target).count("1") <= i <= target:
                return i
        return -1