class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.l = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.l.pop(self.l.index(self.cache[key]))
        self.l.append(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        new = Node(key, value)
        if key in self.cache:
            self.l.pop(self.l.index(self.cache[key]))
        else:
            if self.cap == len(self.cache):
                to_pop = self.l.pop(0)
                del self.cache[to_pop.key]
            
        self.l.append(new)
        self.cache[key] = new
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)