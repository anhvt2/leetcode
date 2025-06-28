# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         cumSum = {0: 1}
#         ans = 0
#         rsum = 0
#         for num in nums:
#             rsum += num
#             if rsum - k in cumSum:
#                 ans += cumSum[rsum - k]
#             cumSum[rsum] = cumSum.get(rsum, 0) + 1
#         return ans

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hashmap to store the count of prefix sums
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Initialize the prefix sum of 0 (for subarrays starting at index 0)
        
        current_sum = 0  # Current running sum
        result = 0  # The count of subarrays whose sum equals to k
        
        for num in nums:
            current_sum += num  # Update the running sum
            
            # If (current_sum - k) is in the hashmap, it means we've found a subarray that sums to k
            if current_sum - k in prefix_sum_count:
                result += prefix_sum_count[current_sum - k]
            
            # Update the hashmap with the current running sum
            prefix_sum_count[current_sum] += 1
        
        return result
