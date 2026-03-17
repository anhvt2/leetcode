class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Idea:
        # Treat each column as a histogram of consecutive 1s ending at current row.
        # heights[j] = number of consecutive 1s in column j up to this row.
        #
        # Since columns can be rearranged independently per row,
        # we can sort the heights descending to place taller columns together.
        #
        # For sorted heights h1 ≥ h2 ≥ ... ≥ hn:
        # possible rectangle areas = height[i] * (i+1)
        # (use the first i+1 columns as width).

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for r in range(m):
            # update histogram heights
            for c in range(n):
                if matrix[r][c] == 0:
                    heights[c] = 0
                else:
                    heights[c] += 1

            # rearrange columns → sort heights
            sorted_h = sorted(heights, reverse=True)

            # compute best rectangle using first k columns
            for k in range(n):
                ans = max(ans, sorted_h[k] * (k + 1))

        return ans