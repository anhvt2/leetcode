class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = format(n, '02b')
        num = 0
        for _, char in enumerate(str(binary)):
            if char == '1':
                num += 1
        return num