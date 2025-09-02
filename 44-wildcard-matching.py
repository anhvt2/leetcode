from typing import List
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0                 # i over s, j over p
        star = -1                 # last position of '*' in p (or -1 if none)
        match = 0                 # position in s corresponding to that '*'

        while i < len(s):
            # direct match or '?'
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # record a '*' and move pattern pointer
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            # mismatch: backtrack if we had a previous '*'
            elif star != -1:
                j = star + 1      # let '*' absorb one more char
                match += 1
                i = match
            else:
                return False

        # consume trailing '*' in pattern
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
