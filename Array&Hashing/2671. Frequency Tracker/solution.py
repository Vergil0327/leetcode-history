class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int)
        self.freq = defaultdict(int)
        
    def add(self, number: int) -> None:
        if number in self.counter:
            self.freq[self.counter[number]] -= 1
            if self.freq[self.counter[number]] == 0:
                del self.freq[self.counter[number]]
        
        self.counter[number] += 1
        self.freq[self.counter[number]] += 1
        
    def deleteOne(self, number: int) -> None:
        if number not in self.counter: return
        
        self.freq[self.counter[number]] -= 1
        if self.freq[self.counter[number]] == 0:
            del self.freq[self.counter[number]]

        self.counter[number] -= 1
        if self.counter[number] == 0:
            del self.counter[number]
        if number in self.counter:
            self.freq[self.counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq
