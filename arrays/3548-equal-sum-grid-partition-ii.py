class Solution:
  def canPartitionGrid(self, grid: list[list[int]]) -> bool:
    # total sum of all elements
    summ = sum(map(sum, grid))

    def canPartition(grid: list[list[int]]) -> bool:
      # Idea:
      # - Treat this as checking ONLY horizontal cuts
      # - We will rotate / reverse grid to reuse this for all directions
      # - Maintain prefix sum (top) and infer bottom = total - top
      # - Use a set to track available values for "remove one cell" case

      topSum = 0
      seen = set()  # values in the "top" part so far

      for i, row in enumerate(grid):
        topSum += sum(row)
        botSum = summ - topSum

        # add current row values into "top"
        seen |= set(row)

        diff = topSum - botSum  # want diff == 0 OR removable

        # Case 1: already equal
        # Case 2: 1D edge cases (only endpoints removable)
        #   - grid[0][0]: top-left corner
        #   - grid[0][-1]: top-right corner (first row)
        #   - row[0]: leftmost element of current boundary row
        if diff in (0, grid[0][0], grid[0][-1], row[0]):
          return True

        # Case 3: general 2D case
        # - if width > 1 and not first row → top part is 2D
        # - we can remove ANY value if it exists in "top"
        if len(grid[0]) > 1 and i > 0 and diff in seen:
          return True

      return False

    # Try all 4 orientations:
    # - original → horizontal cut
    # - reversed → bottom-up cut
    # - transpose → vertical cut
    # - reversed transpose → other vertical direction
    return (canPartition(grid) or
            canPartition(grid[::-1]) or
            canPartition(list(zip(*grid))[::-1]) or
            canPartition(list(zip(*grid))))