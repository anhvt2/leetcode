class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # If the start index reaches the end, we have a valid permutation
            if start == len(nums):
                res.append(nums[:]) # Deep copy the current arrangement
                return
            
            # Try swapping every index from start to the end, as long as they are unique
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                # Swap current number with start index
                nums[start], nums[i] = nums[i], nums[start]

                # Recurse with next start index
                backtrack(start+1)

                # Backtrack: undo the swap
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res