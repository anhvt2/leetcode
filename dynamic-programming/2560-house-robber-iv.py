class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def can(cap: int) -> bool: # cap: capacity
            # greedy: pick any house <= cap, skipping to the next to avoid adjacency
            count = 0
            i = 0
            while i < n:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1 
                if count >= k:
                    return True
            return False
        
        # binary search for cap
        lo, hi = min(nums), max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1 
        return lo