# from typing import List, Optional
# from collections import Counter

# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:

#         def count_vowel(ss): 
#             # Parameters
#             # ----------
#             # ss: substring
#             # Return
#             # ------
#             # vowel_count: number of vowels contained within substring
#             counter = Counter(ss)
#             vowel_count = 0
#             for vowel in ['a', 'e', 'i', 'o', 'u']:
#                 vowel_count += counter[vowel]
#             return vowel_count

#         n = len(s)
#         if k > n:
#             return 0

#         max_vowel = 0
#         for i in range(n-k+1):
#             ss = s[i:i+k]
#             max_vowel = max(max_vowel, count_vowel(ss))

#         return max_vowel

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current_count = 0
        max_count = 0

        for i in range(len(s)):
            if s[i] in vowels:
                current_count += 1
            # sliding window technique
            if i >= k and s[i-k] in vowels: # if lost a vowel then count as loss
                current_count -= 1
            max_count = max(max_count, current_count)

        return max_count

sol = Solution()
s = "weallloveyou"
k = 7
result = sol.maxVowels(s, k)
print(result)
