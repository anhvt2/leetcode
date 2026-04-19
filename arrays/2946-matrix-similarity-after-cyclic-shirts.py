
from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])  # number of columns
        k = k % n  # cyclic shift repeats every n steps
        
        for i, row in enumerate(mat):
            for j in range(n):
                # Even rows (0, 2, 4...): shift LEFT k times
                # After k left shifts, element at j comes from position (j+k)%n
                if i % 2 == 0:
                    if row[j] != row[(j + k) % n]:
                        return False
                
                # Odd rows (1, 3, 5...): shift RIGHT k times  
                # After k right shifts, element at j comes from position (j-k)%n
                else:
                    if row[j] != row[(j - k + n) % n]:
                        return False
        
        return True