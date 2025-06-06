# import random

# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         # brute force: search for len(s)!
#         for c in 'abcdefghijklmnopqrstuvwxyz':
#             if len(s) % 2 == 1 and s.count(c) > len(s) // 2 + 1:
#                 return ""
#             elif len(s) % 2 == 0 and s.count(c) > len(s) // 2:
#                 return ""
#         n = len(s)

#         def checkDupl(s):
#             for i in range(n-1):
#                 if s[i] == s[i+1]:
#                     return True
#             else:
#                 return False

#         def swap(s,r1,r2):
#             if r1 > r2:
#                 r1, r2 = r2, r1
#             t = s[:r1] + s[r2] + s[r1+1:r2] + s[r1] + s[r2+1:]
#             return t

#         while checkDupl(s):
#             r1 = random.randint(0, n-1)
#             r2 = random.randint(0, n-1)
#             while r2 == r1:
#                 r2 = random.randint(0, n-1)
#             s = swap(s,r1,r2)

#         return s

from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        freq = Counter(s)
        n = len(s)

        # Step 2: Early check - if the most frequent char is too frequent, it's impossible
        max_freq = max(freq.values())
        if max_freq > (n + 1) // 2:
            return ""

        # Step 3: Sort characters by frequency (highest first)
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])

        # Step 4: Initialize empty result array
        res = [''] * n
        idx = 0

        # Step 5: Fill characters one by one, skipping every other index
        for char, count in sorted_chars:
            for _ in range(count):
                res[idx] = char
                idx += 2
                if idx >= n:
                    idx = 1  # wrap around to fill odd indices after even ones

        return ''.join(res)



# You throw all your characters into a bag.
# When you reach in, you always pull out the one with the highest frequency.

s = "rvhrlpiesrrryrbrrrrrxrkirranrrrrbdrrzgasoxrrr"
sol = Solution()
print(sol.reorganizeString(s))
