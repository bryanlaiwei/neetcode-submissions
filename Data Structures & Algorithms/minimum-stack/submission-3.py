class MinStack:
    def __init__(self):
        self.stack = []
        self.helpStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.helpStack:
            self.helpStack.append(val)
        elif self.helpStack[-1] < val:
            self.helpStack.append(self.helpStack[-1])
        else:
            self.helpStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.helpStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helpStack[-1]
