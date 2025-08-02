class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = k
        self.front = self.rear = self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return - 1
        else:
            return self.q[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()