class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix) # num rows

        # helper: count how many elements <= mid
        # by walking from bottom-left to top-right in O(n)
        # counting by columns
        def countLE(mid: int) -> int:
            count =  0
            row, col = n-1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # if matrix[row][col] <= mid, then all elements above in that column (0 ... row) are <= mid, so add row+1 to the count, move right
                    count += row + 1
                    col += 1
                else:
                    # this element is too big, go up
                    row -= 1
            return count

        # binary search on the value range [smallest, largest]
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if countLE(mid) < k:
                low = mid+1
            else:
                high = mid
        return low