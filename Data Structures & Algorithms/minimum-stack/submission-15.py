class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            if val <= self.mins[-1]:
                self.mins.append(val)

    def pop(self) -> None:
        current = self.stack.pop()
        if self.mins and self.mins[-1] == current:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
