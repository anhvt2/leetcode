class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s = str(bin(n)[2:])
        c = ""
        for _, ch in enumerate(s):
            if ch == "0":
                c += "1"
            else:
                c += "0"
        return int(c, 2)