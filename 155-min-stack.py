class MinStack:

    def __init__(self):
        self.stack = []  # This is the main stack to store all the values.
        self.min_stack = []  # This is the auxiliary stack to store minimum values.

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the main stack.
        if not self.min_stack or val <= self.min_stack[-1]:  # If the min_stack is empty or the current value is smaller than or equal to the current minimum.
            self.min_stack.append(val)  # Push the value onto the min_stack.

    def pop(self) -> None:
        if self.stack:
            popped_val = self.stack.pop()  # Pop the value from the main stack.
            if popped_val == self.min_stack[-1]:  # If the popped value is the same as the top of the min_stack, pop from min_stack as well.
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]  # Return the top element of the main stack.

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]  # Return the top element of the min_stack, which contains the minimum value.
