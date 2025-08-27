class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # If already all zero, we don't need any queries
        if all(x==0 for x in nums):
            return 0

        n = len(nums)
        # S[i]: indexed set of achievable total decrements on index i using processed queries
        S = [set([0]) for _ in range(n)]
        for k, (l, r, val) in enumerate(queries, start=1):
            # For each i covered by this query, fold in '+val' to all existing sums at i
            for i in range(l, r+1):
                # create the new sum {x+val}
                add = {x+val for x in S[i]}
                # union them
                # S[i] = S[i].union(add) 
                S[i] |= add
            # check if all targets are now achievable
            if all(nums[i] in S[i] for i in range(n)):
                return k
            
        return -1
