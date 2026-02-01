# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow
        prev = None
        nex = second.next
        while second.next:
            second.next = prev
            prev = second
            second = nex
            nex = nex.next
        second.next = prev

        first = head
        nex1 = first.next
        nex2 = second.next

        while second.next:
            first.next = second
            first = nex1
            nex1 = nex1.next
            second.next = first
            second = nex2
            nex2 = nex2.next

        return head  