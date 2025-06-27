from collections import Counter
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each element
        count = Counter(nums)
        
        # Step 2: Find the element(s) with the maximum frequency
        max_freq = max(count.values())
        
        # Step 3: Track the first and last occurrence of each element
        first_occurrence = {}
        last_occurrence = {}
        
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i  # Mark first occurrence
            last_occurrence[num] = i  # Keep updating the last occurrence
        
        # Step 4: Find the smallest subarray that contains all occurrences of the most frequent element
        min_length = float('inf')
        
        for num in count:
            if count[num] == max_freq:
                # Calculate the length of the subarray for this number
                length = last_occurrence[num] - first_occurrence[num] + 1
                min_length = min(min_length, length)
        
        return min_length
