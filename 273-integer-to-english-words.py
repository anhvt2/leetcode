class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                    "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        units = [(10**12, "Trilion"), (10**9, "Billion"), (10**6, "Million"), (1000, "Thousand"), (1, "")]

        def three_digits_to_words(n: int) -> str:
            # n is in [0, 999]
            res = []
            if n >= 100:
                res.append(below_20[n // 100] + " Hundred")
                n %= 100
            if n >= 20:
                res.append(tens[n // 10])
                if n % 10:
                    res.append(below_20[n % 10])
            elif n > 0:
                res.append(below_20[n])
            return " ".join(res)

        ans = []
        for value, name in units:
            if num >= value:
                chunk = num // value
                num = num % value
                if chunk:
                    ans.append(three_digits_to_words(chunk) + (f" {name}" if name else ""))
        s = " ".join(ans)
        return s
