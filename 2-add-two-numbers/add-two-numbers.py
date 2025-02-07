# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        res = ListNode(0)
        cur = res
        carry = 0
        while h1 != None or h2 != None:
            h1val = h1.val if h1 else 0
            h2val = h2.val if h2 else 0

            cSum = h1val + h2val + carry
            carry = cSum // 10

            cur.next = ListNode(cSum % 10)
            cur = cur.next

            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
        
        if carry:
            cur.next = ListNode(carry)
            
        return res.next