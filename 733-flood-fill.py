from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque()
        m = len(image)
        n = len(image[0])
        c = image[sr][sc]
        if c == color:
            return image

        queue.append([sr,sc])
        image[sr][sc] = color
        while queue:
            i, j = queue.popleft()
            for (dr, dc) in [(0,1), (0,-1), (1,0), (-1,0)]:
                ii, jj = i+dr, j+dc
                if 0 <= ii < m and 0 <= jj < n and image[ii][jj] == c:
                    image[ii][jj] = color
                    queue.append([ii, jj])
        return image
