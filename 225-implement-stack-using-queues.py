class MyStack:

    def __init__(self):
        self.stack = []        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if not self.empty() else -1

    def top(self) -> int:
        return self.stack[-1] if not self.empty() else -1

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()