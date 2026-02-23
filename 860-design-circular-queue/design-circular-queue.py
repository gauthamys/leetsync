class ListNode:
    def __init__(self, val, prev=None, nex=None):
        self.val = val
        self.prev = prev
        self.next = nex

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = ListNode(-1)
        self.rear = ListNode(-1)
        self.front.next, self.rear.prev = self.rear, self.front
        self.cap, self.size = k, 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.cap:
            return False
        self.size += 1
        node = ListNode(value)
        node.prev = self.rear.prev
        self.rear.prev.next = node
        node.next = self.rear
        self.rear.prev = node
        return True
    

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        self.front.next = self.front.next.next
        self.front.next.prev = self.front
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.front.next.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.rear.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()