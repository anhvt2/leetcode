class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking (DFS)
        # At each step, try to include a candidate and recurse
        # Stop if total > target
        # If total = target: valid combination

        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:]) # make a copy
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i]) # reuse the same i
                path.pop() # backtrack
            
        backtrack(0, [], 0)
        return res
        # Time complexity: O(2^len(target))
