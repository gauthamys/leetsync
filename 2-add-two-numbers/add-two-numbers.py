# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        res = ListNode(-1)
        cur = res
        carry = 0
        while h1 or h2:
            h1Val = h1.val if h1 else 0
            h2Val = h2.val if h2 else 0
            
            s = h1Val + h2Val + carry
            carry = s // 10

            cur.next = ListNode(s % 10)
            cur = cur.next
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
        if carry:
            cur.next = ListNode(carry)
        
        return res.next
        
