class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sums = [sum(row) for row in grid]
        # col_sums = [sum(grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])) )]
        # Or more explicitly for columns:
        m, n = len(grid), len(grid[0])
        col_sums = [sum(row[j] for row in grid) for j in range(n)]

        def equal_array(array):
            if sum(array) % 2 == 1:
                return False
            
            target = sum(array) // 2
            prefix_sum = 0
            for i in range(len(array)):
                prefix_sum += array[i] # O(1) update
                if prefix_sum == target:
                    return True
            return False

        return equal_array(row_sums) or equal_array(col_sums)
