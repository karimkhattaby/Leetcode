class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minimum and x >= self.minimum[-1]:
            self.minimum.append(self.minimum[-1])
        else:
            self.minimum.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()