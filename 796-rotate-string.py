from collections import Counter, deque

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if Counter(s) != Counter(goal) or len(s) != len(goal):
            return False
        n = len(s)
        queue_g = deque(goal)
        queue_s = deque(s)
        for i in range(n):
            if queue_s == queue_g:
                return True
            else:
                last = queue_g.pop()
                queue_g.appendleft(last)
        return False
        