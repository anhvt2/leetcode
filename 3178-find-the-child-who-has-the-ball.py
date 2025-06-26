class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        pointer = 0  # Start at position 0
        incr = 1  # Start moving forward (increment)

        # Loop k times to simulate the movement
        for i in range(k):
            if 0 <= pointer <= n - 1:  # Ensure the pointer stays within valid bounds
                pointer += incr
            if pointer == n:  # If pointer reaches n, change direction to move backward
                pointer = n - 2
                incr = -1
            elif pointer == -1:  # If pointer reaches -1, change direction to move forward
                pointer = 1
                incr = 1
        
        return pointer
