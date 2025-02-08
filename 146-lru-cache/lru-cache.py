class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, node):
        tmp = self.tail.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.tail
        self.tail.prev = node


    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        print('get', key)
        if key in self.cache.keys():
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        print('put', key)
        if key in self.cache.keys():
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return
        
        if len(self.cache.keys()) == self.capacity:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)

        new = ListNode(key, value)
        self.cache[key] = new
        self.add(new)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)