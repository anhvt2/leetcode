# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         queue = deque()
#         if numRows == 1:
#             return [[1]]
#         elif numRows == 2:
#             return [[1], [1,1]]
#         elif numRows == 3:
#             return [[1], [1,1], [1,2,1]]
#         else:
#             queue.append([1])
#             queue.append([1,1])
#             lastSeq = queue[-1]
#             while len(lastSeq) < numRows - 1:
#                 lastSeq = queue[-1]
#                 nextSeq = deque()
#                 for i in range(len(lastSeq)-1):
#                     nextSeq.append(lastSeq[i] + lastSeq[i+1])
#                 nextSeq.appendleft(1)
#                 nextSeq.append(1)
#                 queue.append(list(nextSeq))
#             return list(queue)

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for row_num in range(numRows):
            # Start each row with '1'
            row = [1] * (row_num + 1) # note the length of the row
            # Fill in the inner elements using previous row
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle
