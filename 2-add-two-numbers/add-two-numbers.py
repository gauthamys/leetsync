# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        tmp = res
        c = 0
        while l1 and l2:
            s = l1.val + l2.val + c
            c = s // 10
            tmp.next = ListNode(s % 10)
            tmp = tmp.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                s = l1.val + c
                tmp.next = ListNode(s % 10)
                c = s // 10
                tmp = tmp.next
                l1 = l1.next
        if l2:
            while l2:
                s = l2.val + c
                tmp.next = ListNode(s % 10)
                c = s // 10
                tmp = tmp.next
                l2 = l2.next
        if c:
            tmp.next = ListNode(c)
        return res.next