class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Idea:
        # Happy strings: adjacent characters must differ.
        # Alphabet = {a, b, c}.
        #
        # Total count:
        # first char: 3 choices
        # each next char: 2 choices (cannot equal previous)
        # total = 3 * 2^(n-1)
        #
        # Generate the k-th string in lexicographic order without generating all.
        # Greedily decide each character using combinatorics.

        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        res = []
        prev = ""

        for i in range(n):
            for c in "abc":
                if c == prev:
                    continue

                # remaining positions after choosing c
                remaining = n - i - 1
                count = 1 << remaining  # number of valid completions

                if k > count:
                    # skip this block
                    k -= count
                else:
                    # choose this character
                    res.append(c)
                    prev = c
                    break

        return "".join(res)