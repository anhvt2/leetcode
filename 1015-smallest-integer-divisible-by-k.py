class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # If k is divisible by 2 or 5, it is IMPOSSIBLE
        # for a number consisting only of '1's (1, 11, 111, ...) to be divisible by k.
        # Because such numbers always end with digit '1', so they are never multiples of 2 or 5.
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rem = 0  # This will store the remainder of the constructed number modulo k
        
        # We try at most k steps because:
        # There are only k possible remainders: 0, 1, 2, ..., k-1.
        # If we repeat a remainder before hitting 0, we are in a cycle → impossible.
        for length in range(1, k + 1):
            # Append a '1' to the right of the current number.
            # Mathematically: new_number = old_number * 10 + 1
            # Instead of storing the number, we only track the remainder modulo k.
            rem = (rem * 10 + 1) % k
            
            # If the remainder becomes 0, the number is divisible by k.
            if rem == 0:
                return length  # The length of the smallest repunit divisible by k
        
        # If we finish loop without finding remainder 0, it is impossible.
        return -1
