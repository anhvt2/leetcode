class Solution:
    def maxOperations(self, s: str) -> int:
        """
        The algorithm processes the string from left to right, tracking the number of '1's seen so far (ones). It looks for '0's that are either:
            - At the end of the string, or
            - Immediately followed by a '1'
        When such a '0' is found, it means we can pair it with any of the previously seen '1's to form a "10" or "01" pair and perform an operation.
        """
        ans = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones += 1
            elif i + 1 == len(s) or s[i + 1] == '1':
                ans += ones
        return ans
