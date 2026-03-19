
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # map (depth, position) -> node value
        tree = {}
        for num in nums:
            d = num // 100
            p = (num // 10) % 10
            v = num % 10
            tree[(d, p)] = v
        
        self.total = 0
        
        def dfs(d, p, curr_sum):
            # if node doesn't exist, stop
            if (d, p) not in tree:
                return
            
            # update path sum
            curr_sum += tree[(d, p)]
            
            # compute children positions
            left = (d + 1, 2 * p - 1)
            right = (d + 1, 2 * p)
            
            # if leaf (no children), add to result
            if left not in tree and right not in tree:
                self.total += curr_sum
                return
            
            # recurse
            dfs(d + 1, 2 * p - 1, curr_sum)
            dfs(d + 1, 2 * p, curr_sum)
        
        # start from root (depth=1, position=1)
        dfs(1, 1, 0)
        
        return self.total