class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        queue = deque()
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        elif numRows == 3:
            return [[1], [1,1], [1,2,1]]
        else:
            queue.append([1])
            queue.append([1,1])
            lastSeq = queue[-1]
            while len(lastSeq) < numRows - 1:
                lastSeq = queue[-1]
                nextSeq = deque()
                for i in range(len(lastSeq)-1):
                    nextSeq.append(lastSeq[i] + lastSeq[i+1])
                nextSeq.appendleft(1)
                nextSeq.append(1)
                queue.append(list(nextSeq))
            return list(queue)
