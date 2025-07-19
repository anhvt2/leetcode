
from typing import List, Optional

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if len(intervals) == 1:
#             return intervals
#         for i in range(len(intervals)-1):
#             for j in range(i+1, len(intervals)+1):
#                 print(i,j)
#                 if intervals[i][0] < intervals[j][0] <= intervals[i][1] < intervals[j][1]:
#                     intervals[i][1] = intervals[j][1]
#                     intervals.pop(j)
#                 elif intervals[j][0] < intervals[i][0] <= intervals[j][1] < intervals[i][1]:
#                     intervals[i][0] = intervals[j][0]
#                     intervals.pop(j)
#                 return intervals

# from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Step 1: Sort intervals by start time
#         intervals.sort(key=lambda x: x[0])

#         merged = [intervals[0]]

#         for current in intervals[1:]:
#             prev = merged[-1]
#             if current[0] <= prev[1]:
#                 # Overlap → merge
#                 prev[1] = max(prev[1], current[1])
#             else:
#                 # No overlap → add as new interval
#                 merged.append(current)

#         return merged

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # Sort by left values
#         intervals.sort(key=lambda x: x[0]) 
#         merged = [intervals[0]]
        
#         for current in intervals[1:]:
#             last = merged[-1]
#             if current[0] <= last[1]:
#                 # Update bounds if overlap, including subset cases
#                 merged[-1][1] = max(merged[-1][1], current[1])
#             else:
#                 merged.append(current)
#         return merged

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        res = []
        
        tmp_start, tmp_end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            if current_start <= tmp_end:
                current_end = max(tmp_end, tmp_end)
            else:
                res.append([tmp_start, tmp_end])
                tmp_start, tmp_end = current_start, current_end
            
        res.append([tmp_start, tmp_end])
        return res

sol = Solution()
# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[15,18],[8,10],[1,3],[2,6]]
# intervals = [[1,4],[4,5]]
result = sol.merge(intervals) # [[1,6],[8,10],[15,18]]
print(result)
