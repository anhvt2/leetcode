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


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def backtrack(path, used):
#             # If path is full length, we found a valid permutation
#             if len(path) == len(nums):
#                 res.append(path[:])  # Make a copy since path will change
#                 return

#             # Try each number
#             for i in range(len(nums)):
#                 if i in used:
#                     continue  # Skip already used numbers

#                 # Choose nums[i]
#                 used.add(i)
#                 path.append(nums[i])
#                 # Explore further
#                 backtrack(path, used)
#                 # Undo choice
#                 path.pop()
#                 used.remove(i)

#         # Start with empty path and empty used set
#         backtrack([], set())
#         return res
