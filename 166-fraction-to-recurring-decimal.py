class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        n, d = abs(numerator), abs(denominator)

        # integer part
        q, r = divmod(n, d)
        res.append(str(q))
        if r == 0:
            return ''.join(res)

        res.append('.')

        # fractional part with cycle detection
        pos = {}  # remainder -> index in res where its digit starts
        while r != 0:
            if r in pos:
                idx = pos[r]
                res.insert(idx, '(')
                res.append(')')
                break
            pos[r] = len(res)
            r *= 10
            digit, r = divmod(r, d)
            res.append(str(digit))

        return ''.join(res)
