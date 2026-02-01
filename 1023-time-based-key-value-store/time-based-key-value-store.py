class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(value, timestamp)]
        else:
            self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        r = len(self.m[key]) - 1
        while r >= 0 and self.m[key][r][1] > timestamp:
            r -= 1
        return self.m[key][r][0] if r != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)