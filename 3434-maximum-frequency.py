from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # sorted: [2,2,2,3,3,4,4,5,5,10]
        left = 0
        total = 0
        max_freq = 0

        for right in range(len(nums)):
            total += nums[right]

            # while the cost to make all numbers in [left, right] equal to nums[right] exceeds k
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq

# Test it
sol = Solution()
nums = [10,2,3,4,5,5,4,3,2,2]
k = 10
print(sol.maxFrequency(nums, k))  # Output: 4 ✅
