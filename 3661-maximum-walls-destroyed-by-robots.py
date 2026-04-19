class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # sort robots by position to reason about blocking locally
        n = len(robots)
        robot_distance_pairs = sorted(zip(robots, distance), key=lambda x: x[0])
        
        # sort walls to enable binary search counting in O(log n)
        walls.sort()
        
        from functools import cache
        from bisect import bisect_left
        
        @cache
        def dp(robot_idx: int, prev_robot_moved_right: int) -> int:
            # dp over robots from 0..robot_idx
            # prev_robot_moved_right:
            #   0 -> previous robot chose LEFT
            #   1 -> previous robot chose RIGHT
            # needed because it affects how far current robot can extend right
          
            # no robots left
            if robot_idx < 0:
                return 0
          
            current_pos, current_distance = robot_distance_pairs[robot_idx]
          
            # -----------------------
            # option 1: move LEFT
            # -----------------------
            # raw interval: [pos - d, pos]
            left_boundary = current_pos - current_distance
          
            # cannot cross previous robot (blocking)
            if robot_idx > 0:
                prev_pos = robot_distance_pairs[robot_idx - 1][0]
                left_boundary = max(left_boundary, prev_pos + 1)
          
            # count walls in [left_boundary, current_pos]
            l = bisect_left(walls, left_boundary)
            r = bisect_left(walls, current_pos + 1)
            walls_covered_left = (r - l) + dp(robot_idx - 1, 0)
          
            # -----------------------
            # option 2: move RIGHT
            # -----------------------
            # raw interval: [pos, pos + d]
            right_boundary = current_pos + current_distance
          
            # must consider NEXT robot because it may block depending on its choice
            if robot_idx + 1 < n:
                next_pos, next_distance = robot_distance_pairs[robot_idx + 1]
              
                if prev_robot_moved_right == 0:
                    # next robot could move LEFT → its left reach blocks earlier
                    right_boundary = min(right_boundary, next_pos - next_distance - 1)
                else:
                    # next robot moves RIGHT → only its position blocks
                    right_boundary = min(right_boundary, next_pos - 1)
          
            # count walls in [current_pos, right_boundary]
            l = bisect_left(walls, current_pos)
            r = bisect_left(walls, right_boundary + 1)
            walls_covered_right = (r - l) + dp(robot_idx - 1, 1)
          
            # take best direction
            return max(walls_covered_left, walls_covered_right)
      
        # start from last robot; assume "virtual" next robot moved right
        return dp(n - 1, 1)