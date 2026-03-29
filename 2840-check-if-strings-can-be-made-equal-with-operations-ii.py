from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        def split(s):
            odd = []
            even = []
            for i, ch in enumerate(s):
                if i % 2 == 0:
                    even.append(ch)
                else:
                    odd.append(ch)
            return even, odd

        even_s1, odd_s1 = split(s1)
        even_s2, odd_s2 = split(s2)

        if Counter(even_s1) == Counter(even_s2) and Counter(odd_s1) == Counter(odd_s2):
            return True
        return False