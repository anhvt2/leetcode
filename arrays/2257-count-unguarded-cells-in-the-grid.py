class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int

        Build a grid marking guards(1) and walls(2). Make four passes:
        - Rows: left -> right + right -> left
        - Columns: top -> bottom + bottom -> top
        While sweeping, once you've seen a guard, make subsequent empty cells as guarded until hit a wall or another guard. Finally count empty cells that are not guarded

        time: O(m*n)
        space: O(m*n)
        """
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        guarded = [[False] * n for _ in range(m)]

        # sweep rows
        for i in range(m):
            seen = False
            for j in range(n):
                if grid[i][j] == 2: # wall
                    seen = False
                elif grid[i][j] == 1: # guard
                    seen = True
                elif seen:
                    guarded[i][j] = True

            seen = False
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 2: # wall
                    seen = False
                elif grid[i][j] == 1: # guard
                    seen = True
                elif seen:
                    guarded[i][j] = True

        # sweep columns
        for j in range(n):
            seen = False
            for i in range(m):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 1:
                    seen = True
                elif seen:
                    guarded[i][j] = True

            seen = False
            for i in range(m-1, -1, -1):
                if grid[i][j] == 2:
                    seen = False
                elif grid[i][j] == 1:
                    seen = True
                elif seen:
                    guarded[i][j] = True

        # count unguarded empties
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not guarded[i][j]:
                    count += 1
        return count

