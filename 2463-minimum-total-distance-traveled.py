class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """
        Calculate the minimum total distance to repair all robots using available factories.
      
        Args:
            robot: List of robot positions
            factory: List of [position, capacity] for each factory
          
        Returns:
            Minimum total distance for all robots to reach factories
        """
      
        @cache
        def dp(robot_idx: int, factory_idx: int) -> int:
            """
            Dynamic programming function to find minimum distance.
          
            Args:
                robot_idx: Current index of robot being considered
                factory_idx: Current index of factory being considered
              
            Returns:
                Minimum distance to repair robots from robot_idx onwards
                using factories from factory_idx onwards
            """
            # Base case: All robots have been assigned
            if robot_idx == len(robot):
                return 0
          
            # Base case: No more factories available but robots remain
            if factory_idx == len(factory):
                return float('inf')
          
            # Option 1: Skip current factory
            min_distance = dp(robot_idx, factory_idx + 1)
          
            # Option 2: Use current factory for some robots
            cumulative_distance = 0
            factory_position = factory[factory_idx][0]
            factory_capacity = factory[factory_idx][1]
          
            # Try assigning 1 to capacity robots to current factory
            for num_robots in range(factory_capacity):
                # Check if we have enough robots remaining
                if robot_idx + num_robots >= len(robot):
                    break
              
                # Add distance for current robot to current factory
                cumulative_distance += abs(robot[robot_idx + num_robots] - factory_position)
              
                # Calculate total distance if we assign (num_robots + 1) robots to this factory
                min_distance = min(
                    min_distance,
                    cumulative_distance + dp(robot_idx + num_robots + 1, factory_idx + 1)
                )
          
            return min_distance
      
        # Sort both lists to enable optimal assignment
        robot.sort()
        factory.sort()
      
        # Calculate the minimum total distance
        result = dp(0, 0)
      
        # Clear the cache to free memory
        dp.cache_clear()
      
        return result
