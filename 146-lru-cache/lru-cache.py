class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.tail = ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new = ListNode(key, value)
        self.add(new)
        self.cache[key] = new

        if len(self.cache) > self.cap:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)