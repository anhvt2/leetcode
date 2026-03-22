from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # Idea:
        # - Try all 4 rotations (0°, 90°, 180°, 270°)
        # - After each rotation, check if mat == target
        # - Rotation: transpose + reverse each row (clockwise 90°)

        # Rotate 90° clockwise using direct index mapping
        def rotate_90(m):
            res = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    # (i, j) -> (j, n-1-i)
                    res[j][n-1-i] = m[i][j]
            return res

        # def rotate(m):
        #     # zip(*m) -> transpose; [::-1] -> reverse each row
        #     return [list(row)[::-1] for row in zip(*m)]

        # Try all 4 orientations
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate_90(mat)

        return False

