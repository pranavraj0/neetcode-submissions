class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currentIndex = 0

    def visit(self, url: str) -> None:
        self.history[self.currentIndex+1:] = []
        self.history.append(url)
        self.currentIndex +=1

    def back(self, steps: int) -> str:
        stepsBack = min(steps, self.currentIndex)

        self.currentIndex = self.currentIndex - stepsBack
        return self.history[self.currentIndex] 


    def forward(self, steps: int) -> str:
        stepsForward = min(steps, len(self.history) - 1 - self.currentIndex)
        self.currentIndex = self.currentIndex + stepsForward
        return self.history[self.currentIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)