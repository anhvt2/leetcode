class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = dict()
        con = dict()

        for _, ch in enumerate(s):
            if ch in ['a', 'e', 'i', 'o', 'u']:
                vow[ch] = vow.get(ch, 0) + 1
            else:
                con[ch] = con.get(ch, 0) + 1
        
        max_vow = 0 if not vow else max(vow.values())
        max_con = 0 if not con else max(con.values())
        return max_vow + max_con
        