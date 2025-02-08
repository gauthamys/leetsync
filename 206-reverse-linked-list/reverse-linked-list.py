# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        mid = head
        nex = mid.next
        while nex != None:
            mid.next = prev
            prev = mid
            mid = nex
            nex = nex.next
            
        mid.next = prev
        return mid