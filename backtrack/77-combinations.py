class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            # If the current combination is complete
            if len(path) == k:
                res.append(path[:]) # then make a copy and return
                return
            
            for i in range(start, n+1):
                path.append(i)          # Choose
                backtrack(i+1, path)    # Explore
                path.pop()              # Unchoose (backtrack)
            
        backtrack(1, [])
        return res
