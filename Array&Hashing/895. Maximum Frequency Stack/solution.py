class FreqStack:

    def __init__(self):
        self.currMax = -1
        self.counter = defaultdict(int)
        self.freqStack = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.counter[val] += 1
        self.currMax = max(self.currMax, self.counter[val])
        self.freqStack[self.counter[val]].append(val)

    def pop(self) -> int:
        el = self.freqStack[self.currMax].pop()
        if not self.freqStack[self.currMax]:
            self.currMax -= 1
        self.counter[el] -= 1
        return el
