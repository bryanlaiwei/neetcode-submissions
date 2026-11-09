class MinStack:

    def __init__(self):
        self.stack = []
        self.helpStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.helpStack or 
            val < self.helpStack[-1]): self.helpStack.append(val)
        else: self.helpStack.append(self.helpStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.helpStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helpStack[-1]