class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self):
        self.base = 769
        self.s = [ListNode(-1) for _ in range(self.base)]

    def add(self, key: int) -> None:
        h = key % self.base
        head = self.s[h]
        cur = head
        prev = None
        while cur:
            if cur.val == key:
                return
            prev = cur
            cur = cur.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        h = key % self.base
        head = self.s[h]
        cur = head
        prev = None
        while cur:
            if cur.val == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def contains(self, key: int) -> bool:
        h = key % self.base
        head = self.s[h]
        cur = head
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)