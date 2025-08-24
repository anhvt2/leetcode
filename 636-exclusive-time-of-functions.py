from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []          # stack of running function ids
        prev = 0            # previous timestamp boundary

        for log in logs:
            fid_str, typ, t_str = log.split(':')
            fid = int(fid_str)
            t = int(t_str)

            if typ == 'start':
                # Charge elapsed time since prev to the function currently on CPU
                if stack:
                    res[stack[-1]] += t - prev
                stack.append(fid)
                prev = t
            else:  # 'end'
                # Finish current function; include this timestamp
                f = stack.pop()
                res[f] += t - prev + 1 # length of the interval
                prev = t + 1   # next slice start at t + 1 because t has been used up by res[f]

        return res
