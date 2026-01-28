from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:       
        # Build adjacency lists
        forward = defaultdict(list)
        backward = defaultdict(list)
        
        for u, v, w in edges:
            forward[u].append((v, w))
            backward[v].append((u, w))
        
        # State: (cost, node, switch_used_at_node)
        # switch_used_at_node tracks if we used the switch when arriving at this node
        pq = [(0, 0, -1)]  # -1 means no switch used yet
        dist = {}
        
        while pq:
            cost, node, last_switch = heappop(pq)
            
            if node == n - 1:
                return cost
            
            state = (node, last_switch)
            if state in dist:
                continue
            dist[state] = cost
            
            # Option 1: Use normal forward edges (don't use switch)
            for next_node, weight in forward[node]:
                new_state = (next_node, -1)
                if new_state not in dist:
                    heappush(pq, (cost + weight, next_node, -1))
            
            # Option 2: Use switch at current node when we arrive
            # Only if we didn't just use a switch to get here
            if last_switch != node:
                for prev_node, weight in backward[node]:
                    new_state = (prev_node, node)
                    if new_state not in dist:
                        heappush(pq, (cost + 2 * weight, prev_node, node))
        
        return -1