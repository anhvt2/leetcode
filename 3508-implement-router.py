from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:

    def __init__(self, memoryLimit: int):
        self.cap = memoryLimit
        self.q = deque()                         # FIFO of (source, destination, timestamp)
        self.present = set()                     # to detect duplicates among stored packets
        self.ts = defaultdict(list)              # destination -> nondecreasing list of timestamps
        self.head = defaultdict(int)             # destination -> logical start index in ts[dest]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.present:
            return False

        if self.cap == 0:
            return True  # nothing can be stored; not a duplicate per spec

        if len(self.q) >= self.cap:
            # evict oldest packet
            s0, d0, t0 = self.q.popleft()
            self.present.discard((s0, d0, t0))
            self.head[d0] += 1
            # optional compaction to drop dead prefix
            arr0 = self.ts[d0]
            h0 = self.head[d0]
            if h0 >= 128 and h0 * 2 >= len(arr0):
                self.ts[d0] = arr0[h0:]
                self.head[d0] = 0

        # add new packet
        self.q.append(key)
        self.present.add(key)
        self.ts[destination].append(timestamp)   # timestamps arrive in increasing order
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.present.discard((s, d, t))
        self.head[d] += 1
        # optional compaction
        arr = self.ts[d]
        h = self.head[d]
        if h >= 128 and h * 2 >= len(arr):
            self.ts[d] = arr[h:]
            self.head[d] = 0
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        arr = self.ts.get(destination)
        if not arr:
            return 0
        h = self.head[destination]
        L = bisect_left(arr, startTime, lo=h)
        R = bisect_right(arr, endTime, lo=h)
        return R - L


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)