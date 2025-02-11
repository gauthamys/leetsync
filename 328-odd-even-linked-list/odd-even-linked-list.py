# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        oddHead = head
        evenHead = head.next
        temp = evenHead

        while oddHead.next and evenHead.next:
            oddHead.next = evenHead.next
            oddHead = oddHead.next
            evenHead.next = oddHead.next
            evenHead = evenHead.next
            if oddHead.next is None:
                break
        
        oddHead.next = temp
        return head