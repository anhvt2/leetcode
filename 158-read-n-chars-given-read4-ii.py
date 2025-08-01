class Solution:
    def __init__(self):
        self.q = deque()
    def read(self, buf: List[str], n: int) -> int:
        buf4 = ['']*4
        read_count = 0
        while read_count<n:
            if len(self.q)>0:
                # read from q to buf
                buf[read_count] = self.q.popleft()
                read_count +=1
            else:
                for i in range(read4(buf4)):
                    self.q.append(buf4[i])
                if len(self.q) == 0: # edge case, nothing to load(even read_count not reach n yet)
                    break
        return read_count