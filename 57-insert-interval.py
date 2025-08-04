class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []

        tmp_start, tmp_end = intervals[0]
        for _, interval in enumerate(intervals[1:]):
            curr_start, curr_end = interval
            if curr_start <= tmp_end:
                tmp_end = max(tmp_end, curr_end) # update tmp_end
            else: # tmp_end, curr_start
                res.append([tmp_start, tmp_end])
                tmp_start, tmp_end = curr_start, curr_end # reset

        res.append([tmp_start, tmp_end])
        return res

