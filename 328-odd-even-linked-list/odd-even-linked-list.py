# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        oddHead = head
        evenHead = None if not oddHead else oddHead.next
        tmp = evenHead

        while tmp and tmp.next and oddHead and oddHead.next:
            oddHead.next = oddHead.next.next
            oddHead = oddHead.next
            tmp.next = tmp.next.next
            tmp = tmp.next
        
        oddHead.next = evenHead
        return head