# class Solution:
#     def checkOnesSegment(self, s: str) -> bool:
#         tmp = []
#         for i in range(len(s)):
#             if s[i] == '1':
#                 tmp.append(i) 
#         # Check if tmp is continuously incremental
#         for j in range(len(tmp)-1):
#             if tmp[j+1] != tmp[j]+1:
#                 return False
#         return True

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Check if there is at most one contiguous segment of '1's
        if '01' in s:
            return False
        else:
            return True
