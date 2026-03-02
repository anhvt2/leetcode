class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Step 1: compute trailing zeros per row
        trailing = []
        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: place correct row at each position
        for i in range(n):
            needed = n - 1 - i
            
            j = i
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            # bubble row j up to position i
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps