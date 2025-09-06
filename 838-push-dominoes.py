class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Left -> Right: positive force from 'R'
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] += f

        # Right -> Left: negative force from 'L'
        f = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] -= f

        # Build result by net force
        res = []
        for x in forces:
            if x > 0:
                res.append('R')
            elif x < 0:
                res.append('L')
            else:
                res.append('.')
        return "".join(res)
