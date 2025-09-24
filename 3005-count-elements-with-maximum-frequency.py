class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = dict()
        max_freq = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_freq:
                max_freq = freq[num]

        count = 0
        for num in set(nums):
            if freq[num] == max_freq:
                count += max_freq
        return count