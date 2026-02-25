class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # sort by (number of 1-bits, value)
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))