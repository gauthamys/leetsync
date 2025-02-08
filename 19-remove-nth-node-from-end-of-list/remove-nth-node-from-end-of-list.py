# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        l = prev
        r = prev

        for _ in range(n + 1):
            r = r.next
        
        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return prev.next
        
