from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0]) # numbers of rows, cols

        # what does histogram represntation mean?
        # For a binary matrix after the loop executes
        # 1 0 1 1       1 0 1 1
        # 1 1 1 1  ->   2 1 2 2
        # 1 1 1 0       3 2 3 0

        # Each value now represents the height of a potential rectangle of all 1's 
        # with its bottom-right corner at that position.  For example, the '3' at
        # at position (2,0) means there are 3 consecutive 1's 
        # going upward from that position.              

        for i in range(m):
            for j in range(n):
                if mat[i][j] > 0 and i > 0:
                    mat[i][j] += mat[i - 1][j] # mat[i][j]: How tall is the column of 1s ending at (i, j)?
        
        ans = 0
        for i in range(m):
            st = []  # monotonic stack of column indices
            cnt = 0  # running count of submatrices ending at this row
            for j in range(n):
                # At each j, we: 
                # * add new submatrices ending at (i, j)
                # * subtract some if the current bar is shorter than previous ones (to remove overcounts)

                # Maintain stack with increasing heights
                while st and mat[i][st[-1]] > mat[i][j]:
                    jj = st.pop() # We remove columns (jj) from the stack if their height is greater than the current column.
                    kk = st[-1] if st else -1 # The width over which mat[i][jj] was the minimum bar height — this width is jj - kk
                    # Remove extra rectangles contributed by taller bar
                    cnt -= (mat[i][jj] - mat[i][j]) * (jj - kk) # We must remove rectangles of height (mat[i][jj] - mat[i][j]) and width (jj - kk).
                
                # Add current column's height
                cnt += mat[i][j]
                ans += cnt
                st.append(j)
        
        return ans