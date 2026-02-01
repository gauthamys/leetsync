# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(-1)
        prev.next = head
        l = r = prev
        for _ in range(n):
            r = r.next
        while r and r.next:
            r = r.next
            l = l.next
        l.next = l.next.next
        return prev.next