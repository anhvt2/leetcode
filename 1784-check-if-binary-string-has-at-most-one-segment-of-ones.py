class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Check if there is at most one contiguous segment of '1's
        if '01' in s:
            return False
        else:
            return True
