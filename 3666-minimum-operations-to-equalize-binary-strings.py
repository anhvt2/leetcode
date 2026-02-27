class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # ts[0] → all even zero-count states not yet visited
        # ts[1] → all odd zero-count states not yet visited
        ts = [SortedSet() for _ in range(2)]
        
        # All possible zero counts are from 0 to n
        # Group by parity (important because cur' changes parity deterministically)
        for i in range(n + 1):
            ts[i % 2].add(i)
        
        cnt0 = s.count('0')   # initial state = number of zeros
        
        # remove start state from available states
        ts[cnt0 % 2].remove(cnt0)
        
        # BFS queue over zero-count states
        q = deque([cnt0])
        ans = 0   # BFS level = number of operations
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                
                # If no zeros → done
                if cur == 0:
                    return ans
                
                # We need feasible x:
                # x = number of zeros chosen in this operation
                # 0 ≤ x ≤ min(cur, k)
                # and also k - x ≤ number of ones = n - cur
                # which implies x ≥ k - (n - cur)
                
                # Derive bounds for next zero count:
                # cur' = cur + k - 2x
                # When x is maximal → cur' minimal
                l = cur + k - 2 * min(cur, k)
                
                # When x is minimal → cur' maximal
                r = cur + k - 2 * max(k - n + cur, 0)
                
                # Only states with correct parity are reachable
                # since cur' = cur + k - 2x → parity fixed by (cur + k)
                t = ts[l % 2]
                
                # Efficiently iterate all reachable states in [l, r]
                j = t.bisect_left(l)
                while j < len(t) and t[j] <= r:
                    nxt = t[j]
                    q.append(nxt)
                    t.remove(nxt)  # mark visited
            
            ans += 1   # next BFS layer
        
        return -1