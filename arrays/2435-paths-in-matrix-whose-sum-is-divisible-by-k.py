from typing import List

MOD = 10**9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        # dp_row[j][r] = number of ways to reach cell (current_i, j) with sum % k == r
        dp_row = [ [0]*k for _ in range(n) ]
        
        # initialize first cell (0,0)
        dp_row[0][ grid[0][0] % k ] = 1
        
        # first row (i = 0), fill left to right using only left cell
        for j in range(1, n):
            val = grid[0][j] % k
            new_arr = [0]*k
            for r in range(k):
                if dp_row[j-1][r]:
                    new_r = (r + val) % k
                    new_arr[new_r] = (new_arr[new_r] + dp_row[j-1][r]) % MOD
            dp_row[j] = new_arr
        
        # process remaining rows
        for i in range(1, m):
            # new_row will be computed for row i; start with first column using only top cell
            new_row = [ [0]*k for _ in range(n) ]
            # handle column 0: can only come from dp_row[0] (the previous row's column 0)
            val = grid[i][0] % k
            for r in range(k):
                if dp_row[0][r]:
                    new_r = (r + val) % k
                    new_row[0][new_r] = (new_row[0][new_r] + dp_row[0][r]) % MOD
            
            # handle columns 1..n-1: come from left (new_row[j-1]) and top (dp_row[j])
            for j in range(1, n):
                add_val = grid[i][j] % k
                # from top (dp_row[j])
                top_arr = dp_row[j]
                if any(top_arr):  # small optimization skip if all zeros
                    for r in range(k):
                        cnt = top_arr[r]
                        if cnt:
                            new_r = (r + add_val) % k
                            new_row[j][new_r] = (new_row[j][new_r] + cnt) % MOD
                # from left (new_row[j-1])
                left_arr = new_row[j-1]
                if any(left_arr):
                    for r in range(k):
                        cnt = left_arr[r]
                        if cnt:
                            new_r = (r + add_val) % k
                            new_row[j][new_r] = (new_row[j][new_r] + cnt) % MOD
            
            # move new_row into dp_row for next iteration (row becomes previous row)
            dp_row = new_row
        
        # result is number of ways reaching bottom-right with remainder 0
        return dp_row[n-1][0] % MOD
