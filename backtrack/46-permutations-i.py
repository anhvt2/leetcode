class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # If start index reaches the end, we have a valid permutation
            if start == len(nums):
                res.append(nums[:])  # Copy the current arrangement
                return

            # Try swapping every index from start to end
            for i in range(start, len(nums)):
                # Swap current number with start index
                nums[start], nums[i] = nums[i], nums[start]

                # Recurse with next start index
                backtrack(start + 1)

                # Backtrack: undo the swap
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res
