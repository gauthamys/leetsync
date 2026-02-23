# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        res = ListNode(0, head)
        l = res
        for _ in range(left - 1):
            l = l.next
        cur = tail = l.next
        prev = r = None
        for _ in range(right - left + 1):
            r = cur.next
            cur.next = prev
            prev = cur
            cur = r
        l.next = prev
        tail.next = r
        return res.next
        