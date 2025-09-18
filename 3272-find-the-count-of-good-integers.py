from typing import List, Tuple

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # precompute factorials up to n
        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1] * i)

        def perms_without_leading_zero(cnt: Tuple[int, ...]) -> int:
            # total permutations: n! / prod(cnt[d]!)
            total = fact[n]
            for c in cnt:
                total //= fact[c]
            # minus those with leading zero, if any
            if cnt[0] == 0:
                return total
            lead0 = fact[n - 1] // fact[cnt[0] - 1]
            for d in range(1, 10):
                lead0 //= fact[cnt[d]]
            return total - lead0

        # enumerate all n-digit palindromes, collect digit count tuples for those divisible by k
        sigs = set()
        half = n // 2
        odd = n % 2

        if n == 1:
            # single-digit palindromes are 1..9
            for d in range(1, 10):
                if d % k == 0:
                    cnt = [0] * 10
                    cnt[d] += 1
                    sigs.add(tuple(cnt))
        else:
            # left half must not start with 0
            start = 10 ** (half - 1)
            end = 10 ** half
            for left in range(start, end):
                s_left = str(left)
                rev = s_left[::-1]
                if odd:
                    for mid in range(10):
                        s = s_left + str(mid) + rev
                        if int(s) % k == 0:
                            cnt = [0] * 10
                            for ch in s:
                                cnt[ord(ch) - 48] += 1
                            sigs.add(tuple(cnt))
                else:
                    s = s_left + rev
                    if int(s) % k == 0:
                        cnt = [0] * 10
                        for ch in s:
                            cnt[ord(ch) - 48] += 1
                        sigs.add(tuple(cnt))

        # sum permutations (no leading zero) over distinct digit multisets
        ans = 0
        for cnt in sigs:
            ans += perms_without_leading_zero(cnt)
        return ans
