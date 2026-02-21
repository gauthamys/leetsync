class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        self.maxFreq = max(self.maxFreq, self.freq[val])
        if self.freq[val] not in self.stks:
            self.stks[self.freq[val]] = []
        self.stks[self.freq[val]].append(val)

    def pop(self) -> int:
        popped = self.stks[self.maxFreq].pop()
        self.freq[popped] -= 1
        if not self.stks[self.maxFreq]:
            del self.stks[self.maxFreq]
            self.maxFreq = max(self.freq.values())
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()