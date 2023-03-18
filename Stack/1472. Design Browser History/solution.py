class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.forwardHistory = []
        

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forwardHistory.clear()

    def back(self, steps: int) -> str:
        while len(self.history) > 1 and steps > 0:
            self.forwardHistory.append(self.history.pop())
            steps -= 1
        return self.history[-1]
        

    def forward(self, steps: int) -> str:
        while self.forwardHistory and steps > 0:
            self.history.append(self.forwardHistory.pop())
            steps -= 1
        return self.history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)