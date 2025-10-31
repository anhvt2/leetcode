class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = {}
        caught = []
        for _, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == 2:
                caught.append(num)
            if len(caught) == 2:
                return caught
        return None