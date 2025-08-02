class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i = 0
        seen = set()
        score = 0 
        n = len(values)
        while not (i < 0 or i >= n or i in seen):
            seen.add(i)
            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == 'jump':
                i += values[i]
        return score