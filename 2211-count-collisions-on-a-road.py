from typing import List
class Solution:
    def countCollisions(self, directions: str) -> int:
        if len(directions) == 1:
            return 0
        
        n = len(directions)
        # skip leading 'L' cars - they move left off the road and never collide
        left = 0
        while left < n and directions[left] == 'L':
            left += 1

        # skip trailing 'R' cars - they move right off the road and never collide
        right = n - 1
        while right > 0 and directions[right] == 'R':
            right -= 1

        # count moving car (non-'S') in the remaining window [left..right]. All remaining 'L's must at some time meet something to their left (either a stationary car or some 'R' coming from left), causing collision(s) and becoming 'S'. Similarly all remaining 'R's must hit something to their right.
        collisions = 0
        for i in range(left, right + 1):
            if directions[i] != 'S':
                collisions += 1

        return collisions
