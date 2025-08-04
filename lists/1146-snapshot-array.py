import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        # for each (index, val), keep a list of (snap_id, val), sorted by snap_id
        # init with [(0,0)] so self.get() returns 0 by default
        self.data = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        tmp = self.data[index]
        # if this index has been set before, then overwrite
        if tmp[-1][0] == self.snap_id:
            tmp[-1] = (self.snap_id, val)
        else:
            tmp.append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        lst = self.data[index]
        # find the right most record with snap_id <= given snap_id
        i = bisect.bisect_right(lst, (snap_id, float('inf'))) - 1
        return lst[i][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)