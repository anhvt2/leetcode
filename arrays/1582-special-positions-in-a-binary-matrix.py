class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Precompute row and column sums
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                # Special position:
                # 1) cell is 1
                # 2) exactly one 1 in its row
                # 3) exactly one 1 in its column
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        
        return count