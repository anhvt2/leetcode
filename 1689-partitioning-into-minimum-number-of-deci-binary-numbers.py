class Solution:
    def minPartitions(self, n: str) -> int:
        # minimum number of deci-binary numbers
        # equals the maximum digit
        return max(int(c) for c in n)