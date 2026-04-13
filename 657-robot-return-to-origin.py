from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        if counter['L'] == counter['R'] and counter['D'] == counter['U']:
            return True
        return False