class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_front(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.size += 1
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.m = {} #(freq, DLL (LRU))
        self.freqs = {} # (key, freq)
        self.nodes = {} # (key, node)
        self.minFreq = float('inf')

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self.m[self.freqs[key]].remove(node)
        self.freqs[key] += 1
        if self.freqs[key] not in self.m:
            self.m[self.freqs[key]] = DLL()
        self.m[self.freqs[key]].insert_front(node)
        if self.m[self.minFreq].size == 0:
            del self.m[self.minFreq]
            self.minFreq = min(self.m.keys())
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.m[self.freqs[key]].remove(node)
            self.freqs[key] += 1
            if self.freqs[key] not in self.m:
                self.m[self.freqs[key]] = DLL()
            self.m[self.freqs[key]].insert_front(node)
            if self.m[self.minFreq].size == 0:
                del self.m[self.minFreq]
                self.minFreq = min(self.m.keys())
        else:
            if len(self.nodes) == self.cap:
                del self.nodes[self.m[self.minFreq].tail.prev.key]
                self.m[self.minFreq].remove(self.m[self.minFreq].tail.prev)
            node = ListNode(key, value)
            self.freqs[key] = 1
            self.minFreq = 1
            if 1 not in self.m:
                self.m[1] = DLL()
            self.m[1].insert_front(node)
            self.nodes[key] = node
        



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)