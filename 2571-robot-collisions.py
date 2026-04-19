class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # sort robots by position to simulate collisions from left -> right
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # keep indices of right-moving robots
        alive = [True] * len(robots)
        
        for i, (pos, hp, d, _) in enumerate(robots):
            if d == 'R':
                # right-moving robot: push to stack, may collide later
                stack.append(i)
            else:
                # left-moving robot: collide with previous right-moving robots
                while stack and robots[i][1] > 0:
                    j = stack[-1]
                    
                    if not alive[j]:
                        stack.pop()
                        continue
                    
                    # compare healths
                    if robots[j][1] < robots[i][1]:
                        # right robot dies, left loses 1 hp
                        alive[j] = False
                        stack.pop()
                        robots[i] = (pos, robots[i][1] - 1, d, robots[i][3])
                    elif robots[j][1] > robots[i][1]:
                        # left robot dies, right loses 1 hp
                        alive[i] = False
                        robots[j] = (robots[j][0], robots[j][1] - 1, robots[j][2], robots[j][3])
                        break
                    else:
                        # both die
                        alive[j] = False
                        alive[i] = False
                        stack.pop()
                        break
        
        # collect survivors in original order
        res = []
        for i, (_, hp, _, idx) in enumerate(robots):
            if alive[i]:
                res.append((idx, hp))
        
        res.sort()  # restore original order
        return [hp for _, hp in res]