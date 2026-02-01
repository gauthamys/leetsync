class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def insert(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __init__(self, capacity: int):
        self.m = {}
        self.cap = capacity
        self.head = self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self.remove(self.m[key])
        node = ListNode(key, self.m[key].val)
        self.m[key] = node
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
            self.insert(self.m[key])
            self.m[key].val = value
            return
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.remove(self.tail.prev)
        node = ListNode(key, value)
        self.m[key] = node
        self.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)