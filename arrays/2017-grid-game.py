class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # O(n) time, O(n) space
        # If the first robot drops from the top row to the bottom row at column i, then:
        # Everything to the right of i on the top row remains for robot 2 → top_total - top_cumu[i].
        # Everything to the left of i on the bottom row remains for robot 2 → bottom_prefix[i-1] (or 0 if i == 0).
        # Robot 1 chooses i to minimize robot 2's maxmimum possible remain points
        # min​ max_{i} (top_total - top_cumu[i], bottom_prefix[i-1])
        # Robot 2 chooses the path with higher points among two possible paths (top-right or bottom-left)
        top, bot = grid[0], grid[1]
        n = len(top)

        top_cumu = [0] * n
        bot_cumu = [0] * n

        sum_top, sum_bot = 0, 0
        for i in range(n):
            sum_top += top[i]
            sum_bot += bot[i]
            top_cumu[i] = sum_top
            bot_cumu[i] = sum_bot
        
        top_total = top_cumu[-1] # last cumulative sum

        pts2 = float('inf') # points for second robot
        for i in range(n):
            # If robot 1 drops to bottom at column i
            # remain on top of the right of i
            top_remain = top_total - top_cumu[i]
            # remain on bottom to the left of i
            bot_remain = bot_cumu[i-1] if i > 0 else 0

            # Robot 2 will take the larger of the two regions
            tmp_best = max(top_remain, bot_remain)
            pts2 = min(tmp_best, pts2)
        return pts2
