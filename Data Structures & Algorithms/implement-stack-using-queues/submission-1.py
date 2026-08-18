class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int: #can't do o(1)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)
        

    def top(self) -> int:
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        toReturn = self.queue[0]
        self.queue.append(self.queue.pop(0))
        return toReturn
        

    def empty(self) -> bool:
        return False if self.queue else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()