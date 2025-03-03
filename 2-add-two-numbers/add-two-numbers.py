# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        carry = 0
        res = ListNode(-1)
        ret = res

        while h1 or h2:
            left = 0 if not h1 else h1.val
            right = 0 if not h2 else h2.val
            s = left + right + carry
            ret.next = ListNode(s % 10)
            ret = ret.next
            carry = s // 10
            if h1:
                h1 = h1.next
            if h2:
                h2 = h2.next
        
        if carry:
            ret.next = ListNode(carry)
            
        return res.next
