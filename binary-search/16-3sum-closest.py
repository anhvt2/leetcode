# sorted triplet: [ nums[i], nums[left], nums[right] ]
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1 # need to increase
                elif curr_sum > target:
                    right -= 1 # need to decrease
                else:
                    return target # exact
        return closest_sum