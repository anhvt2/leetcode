class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicate a
            
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue # skip duplicate b

                left, right = j+1, n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # skip duplicates
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                        
                    elif total < target:
                        left += 1 # increase
                    elif total > target:
                        right -= 1 # decrease
        return res