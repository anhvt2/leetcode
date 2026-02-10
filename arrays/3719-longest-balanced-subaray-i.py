class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Track distinct even numbers seen so far
        seen_even = set()
        
        # Track distinct odd numbers seen so far
        seen_odd = set()

        # balance = (#distinct evens) - (#distinct odds)
        balance = 0

        # Map: balance value → earliest index where it occurred
        # balance 0 at index -1 allows subarrays starting at index 0
        balance_map = {0: -1}

        # Store the maximum length found
        ans = 0

        # Iterate through the array once
        for i, x in enumerate(nums):

            # If x is even
            if x % 2 == 0:
                # Only count x if it is a NEW distinct even
                if x not in seen_even:
                    seen_even.add(x)
                    balance += 1   # increase even count
            else:
                # x is odd
                # Only count x if it is a NEW distinct odd
                if x not in seen_odd:
                    seen_odd.add(x)
                    balance -= 1   # increase odd count (subtract)

            # A subarray nums[l+1 .. r] is balanced iff: balance[r] − balance[l] = 0
            # If this balance has been seen before
            if balance in balance_map:  
                # The subarray between the previous index + 1 and i has equal distinct evens and odds
            else:
                ans = max(ans, i - balance_map[balance])
                # First time seeing this balance → record index
                balance_map[balance] = i

        # Return the longest balanced subarray length
        return ans
