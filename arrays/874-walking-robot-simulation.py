class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Key idea:
        - Simulate robot movement step by step.
        - Directions encoded as:
            0: north, 1: east, 2: south, 3: west
        - Use a set for O(1) obstacle lookup.
        - For each forward command, move one step at a time
          (to correctly stop before hitting obstacle).
        - Track max Euclidean distance squared from origin.

        Time complexity: O(total steps)
        """

        # Directions: N, E, S, W -- indexed by [d] += 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0  # start facing north

        # Convert obstacles to set for fast lookup
        obstacle_set = set(map(tuple, obstacles))

        x = y = 0
        max_dist = 0

        for cmd in commands:
            if cmd == -1:
                # turn right
                d = (d + 1) % 4
            elif cmd == -2:
                # turn left
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]

                # move step by step
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy

                    # stop if obstacle encountered
                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x * x + y * y)

        return max_dist