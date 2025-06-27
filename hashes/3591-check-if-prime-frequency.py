from collections import Counter
import math

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        count = Counter(nums)

        def is_prime(n: int) -> bool:
            if n == 1:
                return False
            i = 2
            while i*i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True
        
        for k, v in count.items():
            if is_prime(v):
                return True
        return False
