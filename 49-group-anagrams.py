# Given an array of strings strs, group the together. You can return the answer in any order.

from typing import List, Optional
from collections import Counter

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         for word in strs:
#             s = strs.pop(0)
#             tmp = [s]
#             for word_ in strs:
#                 if Counter(s) == Counter(word_):
#                     strs.remove(word_)
#                     tmp += [word_]
#             result += [tmp]
#         # return the rest that does not fit
#         for word in strs:
#             result += [[word]]
#         return result

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
return list(anagrams.values())

sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = ["","",""]
result = sol.groupAnagrams(strs)
print(result)

# refs = [["bat"],["nat","tan"],["ate","eat","tea"]]

