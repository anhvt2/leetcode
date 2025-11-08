from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []
        
        # Frequency map of current window
        freq = defaultdict(int)
        
        # Heaps:
        # top_min keeps current top-x keys, ordered by (freq, value) ascending (worst-at-top)
        # rest_max keeps remaining keys, ordered by (-freq, -value) so we pop best first
        top_min = []     # entries: (freq, value, key)
        rest_max = []    # entries: (-freq, -value, key)
        top_set = set()  # keys currently in top
        sum_top = 0      # sum over v * freq[v] for v in top_set
        
        def push_for_key(key):
            """Push the latest state of 'key' into the appropriate heap based on membership."""
            f = freq.get(key, 0)
            if f == 0:
                return
            if key in top_set:
                heapq.heappush(top_min, (f, key, key))
            else:
                heapq.heappush(rest_max, (-f, -key, key))
        
        def clean_top_min():
            """Pop stale entries from top_min until the head matches current (freq, in_top)."""
            while top_min:
                f, _, key = top_min[0]
                if key not in top_set or freq.get(key, 0) != f:
                    heapq.heappop(top_min)
                else:
                    break
        
        def clean_rest_max():
            """Pop stale entries from rest_max until the head matches current (freq, not in top)."""
            while rest_max:
                nf, nk, key = rest_max[0]
                f = -nf
                v = -nk
                if key in top_set or freq.get(key, 0) != f or key != v:
                    heapq.heappop(rest_max)
                else:
                    break
        
        def move_rest_best_to_top():
            """Move the best item from rest into top_set (if any)."""
            nonlocal sum_top
            clean_rest_max()
            if not rest_max:
                return False
            nf, nk, key = heapq.heappop(rest_max)
            f = -nf
            # place into top
            top_set.add(key)
            sum_top += key * f
            heapq.heappush(top_min, (f, key, key))
            return True
        
        def move_top_worst_to_rest():
            """Move the worst item from top into rest."""
            nonlocal sum_top
            clean_top_min()
            if not top_min:
                return False
            f, _, key = heapq.heappop(top_min)
            # remove from top
            if key in top_set:
                top_set.remove(key)
                sum_top -= key * f
                # push to rest
                heapq.heappush(rest_max, (-f, -key, key))
            return True
        
        def better_rest_than_top_worst():
            """Return True if rest's best outranks top's worst."""
            clean_rest_max()
            clean_top_min()
            if not rest_max or not top_min:
                return False
            # Compare rest best (by higher freq, then higher value)
            f_best, v_best, key_best = -rest_max[0][0], -rest_max[0][1], rest_max[0][2]
            f_worst, _, key_worst = top_min[0]
            # rest best is better if freq is greater, or equal freq but value is greater
            if f_best > f_worst:
                return True
            if f_best == f_worst and v_best > key_worst:
                return True
            return False
        
        def rebalance():
            """Ensure |top_set| == min(x, #distinct) and it's the correct top-x by ordering."""
            # Fill up top to size x if possible
            while len(top_set) < x:
                before = len(top_set)
                if not move_rest_best_to_top():
                    break  # no more items outside
                if len(top_set) == before:
                    break
            # If top too large, push worsts out
            while len(top_set) > x:
                moved = move_top_worst_to_rest()
                if not moved:
                    break
            # Swap until top is optimal
            while better_rest_than_top_worst():
                # swap one
                # pull best from rest into top
                move_rest_best_to_top()
                # push worst of top to rest (to keep size ≤ x)
                if len(top_set) > x:
                    move_top_worst_to_rest()
        
        # Initialize first window
        for i in range(k):
            freq[nums[i]] += 1
        # Initially, consider all keys are in "rest", then move best x into "top"
        for key in freq.keys():
            heapq.heappush(rest_max, (-freq[key], -key, key))
        rebalance()
        
        ans = [sum_top]
        
        # Slide the window
        for i in range(k, n):
            out_v = nums[i - k]
            in_v  = nums[i]
            
            # Remove out_v
            if freq[out_v] > 0:
                # If out_v is in top, adjust sum_top first with old count
                if out_v in top_set:
                    sum_top -= out_v * freq[out_v]
                freq[out_v] -= 1
                if freq[out_v] == 0:
                    # if it was in top, also remove membership
                    if out_v in top_set:
                        top_set.remove(out_v)
                    # no need to push; lazy deletion will clear stale entries
                else:
                    # push updated entry back to appropriate heap
                    if out_v in top_set:
                        # still in top: re-add with new freq and update sum_top
                        heapq.heappush(top_min, (freq[out_v], out_v, out_v))
                        sum_top += out_v * freq[out_v]
                    else:
                        heapq.heappush(rest_max, (-freq[out_v], -out_v, out_v))
            
            # Add in_v
            prev_in_top = (in_v in top_set)
            old = freq[in_v]
            new = old + 1
            # If it was in top, remove old contribution first
            if prev_in_top and old > 0:
                sum_top -= in_v * old
            freq[in_v] = new
            # Push updated state
            if prev_in_top:
                heapq.heappush(top_min, (new, in_v, in_v))
                sum_top += in_v * new
            else:
                heapq.heappush(rest_max, (-new, -in_v, in_v))
            
            # Rebalance to restore correct top-x
            rebalance()
            ans.append(sum_top)
        
        return ans
