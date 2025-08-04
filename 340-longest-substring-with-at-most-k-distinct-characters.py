
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n)
        # Idea: implement a counter using dictionary
        # Edge cases
        if k == 0 or not s:
            return 0

        left = 0
        max_len = 0
        freq = defaultdict(int)  # character -> its count in window

        # Expand the window with `right`
        for right, ch in enumerate(s):
            freq[ch] += 1

            # If we have too many distinct chars, shrink from the left
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            # Now window [left..right] has <= k distinct chars
            max_len = max(max_len, right - left + 1)

        return max_len


# Time complexity: O(n^2)
# Space complexity: O(n)
# from typing import List, Optional
# from collections import Counter

# class Solution:
#     def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         # Edge case
#         if not s or k == 0:
#             return 0

#         l = 0
#         max_len = 0
#         # Use r to extend the window one char at a time
#         for r in range(len(s)):
#             window = s[l:r+1]
#             count = Counter(window)
#             while len(count) > k:
#                 l += 1
#                 window = s[l:r+1]
#                 count = Counter(window)
#             max_len = max(max_len, r-l+1)       
#         return max_len
