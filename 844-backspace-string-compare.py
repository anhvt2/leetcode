class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            res = []
            for _, ch in enumerate(s):
                if ch != '#':
                    res.append(ch)
                else:
                    if res:
                        res.pop()
            return "".join(res)
        return backspace(s) == backspace(t)