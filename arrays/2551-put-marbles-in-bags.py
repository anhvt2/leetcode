from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or n <= 1:
            return 0
        
        # if split 'weights' into k bags by placing (k-1) cuts between adjacent marbles, then the total scores = weights[0] + weights[-1] + sum( weights[i] + weights[i+1] for each cut between i and i+1
        # The only thing that changes across the partition is the sum of (k-1) chosen pairs
        # Max score: pick (k-1) largest sum of pairs
        # Min score: pick (k-1) smallest sum of pairs
        pair = [weights[i] + weights[i+1] for i in range(n-1)]
        pair.sort() # ascending

        diff = 0
        for i in range(k-1):
            diff += (pair[-1-i] - pair[i])
        return diff
