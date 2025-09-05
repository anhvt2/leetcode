class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def signature(x: int) -> tuple[int, ...]:
            cnt = [0]*10
            while x:
                cnt[x % 10] += 1
                x //= 10
            return tuple(cnt)

        sigs = set()
        p = 1
        for _ in range(31):          # 2^0 .. 2^30 cover up to 1e9+
            sigs.add(signature(p))
            p <<= 1

        return signature(n) in sigs
