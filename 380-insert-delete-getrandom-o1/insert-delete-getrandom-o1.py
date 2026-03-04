from random import choice
class RandomizedSet:

    def __init__(self):
        self.s = defaultdict(int)
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            last_element = self.vals[-1]
            idx = self.s[val]
            self.vals[idx] = last_element
            self.s[last_element] = idx
            self.vals.pop()
            del self.s[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()