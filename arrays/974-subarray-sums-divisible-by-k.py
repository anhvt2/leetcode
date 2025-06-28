from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_mod_count = defaultdict(int)
        prefix_mod_count[0] = 1  # Initialize with 0 sum having occurred once (important for cases where prefix sum % k == 0)
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num  # Update running sum
            mod = current_sum % k  # Calculate current sum modulo k
            
            # Adjust mod to always be positive, because negative mod can result in negative values
            if mod < 0:
                mod += k
            
            # If mod has been seen before, it means there are subarrays that sum to a multiple of k
            result += prefix_mod_count[mod]
            
            # Increment the count of this mod in the hashmap
            prefix_mod_count[mod] += 1
        
        return result
