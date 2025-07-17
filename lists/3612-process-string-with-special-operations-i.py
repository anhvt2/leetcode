class Solution:
    def processStr(self, s: str) -> str:
        res = ''
        for i, char in enumerate(s):
            if char == '*':
                if res:
                    res = res[:-1]
            elif char == '#':
                res += res
            elif char == '%':
                res = res[::-1]
            else:
                res += char
        return res
