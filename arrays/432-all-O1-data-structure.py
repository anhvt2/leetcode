class Bucket:
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

# A doubly linked list of "buckets" (each bucket = a count + a set of keys)
class AllOne:

    def __init__(self):
        # Sentinels: head.next is min bucket, tail.prev is max bucket
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.loc = {}  # key -> Bucket

    # ----- DLL helpers -----
    def _add_after(self, node: Bucket, newnode: Bucket) -> None:
        newnode.prev = node
        newnode.next = node.next
        node.next.prev = newnode
        node.next = newnode

    def _add_before(self, node: Bucket, newnode: Bucket) -> None:
        self._add_after(node.prev, newnode)

    def _remove_bucket(self, node: Bucket) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # ----- API -----
    def inc(self, key: str) -> None:
        if key in self.loc:
            cur = self.loc[key]
            nxt = cur.next
            # ensure a bucket for count+1 right after cur
            if nxt is self.tail or nxt.count != cur.count + 1:
                nxt = Bucket(cur.count + 1)
                self._add_after(cur, nxt)
            # move key to nxt
            nxt.keys.add(key)
            self.loc[key] = nxt
            cur.keys.remove(key)
            if not cur.keys:
                self._remove_bucket(cur)
        else:
            # need a bucket with count=1 just after head
            first = self.head.next
            if first is self.tail or first.count != 1:
                first = Bucket(1)
                self._add_after(self.head, first)
            first.keys.add(key)
            self.loc[key] = first

    def dec(self, key: str) -> None:
        if key not in self.loc:
            return
        cur = self.loc[key]
        if cur.count == 1:
            # removing key entirely
            del self.loc[key]
            cur.keys.remove(key)
            if not cur.keys:
                self._remove_bucket(cur)
        else:
            prv = cur.prev
            # ensure a bucket for count-1 right before cur
            if prv is self.head or prv.count != cur.count - 1:
                prv = Bucket(cur.count - 1)
                self._add_before(cur, prv)
            prv.keys.add(key)
            self.loc[key] = prv
            cur.keys.remove(key)
            if not cur.keys:
                self._remove_bucket(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        # return any key from the max-count bucket
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        # return any key from the min-count bucket
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()