from typing import List, Optional
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        idxs, vals = [], []
        for i, ch in enumerate(s):
            if ch in vowels:
                idxs.append(i)
                vals.append(ch)
        vals.sort()  # ASCII order satisfies the problem

        # Replace char 'ch' only at index 'idx'
        s_list = list(s)
        for i, ch in zip(idxs, vals):
            s_list[i] = ch
        return "".join(s_list)
