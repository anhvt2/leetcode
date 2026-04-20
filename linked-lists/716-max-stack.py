import heapq
from typing import Optional

# ------------------------
#  Doubly-linked-list node
# ------------------------
class Node:
    """
    Each node stores:
        * val  : the stack value
        * nid  : a unique push-order ID (used to break ties so
                 the most-recent max is removed by popMax)
        * prev / next : links in the doubly-linked list
    """
    __slots__ = ("val", "nid", "prev", "next")

    def __init__(self, val: int, nid: int):
        self.val  = val
        self.nid  = nid
        self.prev = None
        self.next = None

# ------------------------
# Main class
# ------------------------
class MaxStack:

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.heap  = []       # Python heapq (min-heap)
        self.alive = set()    # IDs of nodes still in the list
        self._uid  = 0        # monotonically increasing push ID

    
    def _push_list(self, node: Node) -> None:
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node

    # ---- internal helper: unlink node from the list in O(1) ----
    def _unlink(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # ---- internal helper: discard heap entries whose node was popped ----
    def _clean_heap(self) -> None:
        while self.heap and (-self.heap[0][1]) not in self.alive:
            heapq.heappop(self.heap)

    def push(self, x: int) -> None:
        self._uid += 1
        node = Node(x, self._uid)

        self._push_list(node)
        self.alive.add(node.nid)
        heapq.heappush(self.heap, (-x, -node.nid, node))

    def pop(self) -> int:
        if self.head.next is self.tail:           # empty
            return None
        node = self.tail.prev
        self._unlink(node)
        self.alive.remove(node.nid)
        return node.val
        

    def top(self) -> int:
        return None if self.head.next is self.tail else self.tail.prev.val

    def peekMax(self) -> int:
        self._clean_heap()
        return None if not self.heap else -self.heap[0][0]  

    def popMax(self) -> int:
        self._clean_heap()
        if not self.heap:
            return None
        _, _, node = heapq.heappop(self.heap)
        self._unlink(node)
        self.alive.remove(node.nid)
        return node.val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()