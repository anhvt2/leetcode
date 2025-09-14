class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n > 0:
            if (n & 3) == 3:   # ...11 → add 1 to carry the run of 1s
                n += 1
                ans += 1
            elif n & 1:        # ...01 → subtract 1 to clear the single 1
                n -= 1
                ans += 1
            else:              # ...0  → drop the trailing zero (equiv. to using a big 2^k)
                n >>= 1
        return ans

# class Solution:
#     def minOperations(self, n: int) -> int:
#         def is_set(n, i):
#             return n & (1 << i) != 0
#         #def set_bit(n, i):
#         #    return n | (1 << i)
#         """
#         max n is 100000 < pow(2,20) so lets considering only 20 bits 
#         Algo:
#         1. Traverse over the binary representation of n
#         2. Detect groups of > 1 consecutive zeros. For each such group:
#             a. Increment steps by 1
#             b. Reset all the bits from start,end of the group
#             c. Set the end+1th bit
#         3. Do one more pass and just count the no. of solo 1s remaining and incrment steps by that value
#         """
#         steps = 0
#         # Streak length: end - start + 1
#         streak = 0
#         for bit in range(20):
#             if is_set(n, bit):
#                 # continue the streak
#                 streak += 1
#             else:
#                 # bit is reset
#                 if streak > 1:
#                     # end of a streak
#                     steps += 1
#                     #n = set_bit(n, bit)
#                     streak = 1
#                 else:
#                     steps += streak
#                     streak = 0
#         #for bit in range(20):
#         #    if is_set(n, bit):
#         #        steps += 1
#         return steps 