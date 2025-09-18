import heapq
from typing import List, Dict, Tuple

class TaskManager:
    # tasks: list of [userId, taskId, priority]
    def __init__(self, tasks: List[List[int]]):
        # meta: taskId -> (userId, priority)
        self.meta: Dict[int, Tuple[int, int]] = {}
        # max-heap by (priority desc, taskId desc) -> use negatives for heapq
        # store tuples: (-priority, -taskId, taskId)
        self.heap: List[Tuple[int, int, int]] = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.meta[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.meta[taskId]
        self.meta[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))  # lazy: old entry stays

    def rmv(self, taskId: int) -> None:
        # lazy delete: remove from meta; stale heap entries will be skipped
        if taskId in self.meta:
            del self.meta[taskId]

    def execTop(self) -> int:
        # Pop until we find a heap entry that matches current meta
        while self.heap:
            negp, negid, tid = heapq.heappop(self.heap)
            if tid in self.meta:
                userId, curp = self.meta[tid]
                if -negp == curp:          # up-to-date entry
                    del self.meta[tid]     # remove from system after executing
                    return userId
                # else: stale entry with old priority; keep popping
        return -1
