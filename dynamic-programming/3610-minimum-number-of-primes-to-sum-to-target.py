from math import isqrt

# the sum of the selected primes is exactly n. return the minimum number of prime numbers

class Solution:
    # create an array of primes up until n
    def sieve(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0:2] = [False, False]
        for i in range(2, isqrt(n) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
        return [i for i, val in enumerate(is_prime) if val]
    
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes = self.sieve(n)
        f = [0] + [inf] * n
        for x in primes[:m]:
            for i in range(x, n + 1):
                # f[i] is the minimum number of primes needed to sum up to i
                f[i] = min(f[i], f[i - x] + 1)
        return f[n] if f[n] < inf else -1
