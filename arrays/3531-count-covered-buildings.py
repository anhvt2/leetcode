from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        """
        O(M) time: compute min/max coordinate per row and per column,
        then count buildings that are strictly between min and max on both axes.
        """
        # dictionaries: row_x -> (min_y, max_y), col_y -> (min_x, max_x)
        min_y_in_row = {}
        max_y_in_row = {}
        min_x_in_col = {}
        max_x_in_col = {}

        # 1) single pass to populate min/max for each row and column
        for x, y in buildings:
            # row x
            if x in min_y_in_row:
                if y < min_y_in_row[x]:
                    min_y_in_row[x] = y
                if y > max_y_in_row[x]:
                    max_y_in_row[x] = y
            else:
                min_y_in_row[x] = y
                max_y_in_row[x] = y

            # column y
            if y in min_x_in_col:
                if x < min_x_in_col[y]:
                    min_x_in_col[y] = x
                if x > max_x_in_col[y]:
                    max_x_in_col[y] = x
            else:
                min_x_in_col[y] = x
                max_x_in_col[y] = x

        # 2) count buildings that have strictly smaller and strictly larger neighbors
        ans = 0
        for x, y in buildings:
            # row condition: there must be at least one building with y < current y
            # and at least one building with y > current y
            if not (min_y_in_row[x] < y < max_y_in_row[x]):
                continue
            # column condition: at least one building with x < current x and x > current x
            if not (min_x_in_col[y] < x < max_x_in_col[y]):
                continue
            ans += 1

        return ans
 