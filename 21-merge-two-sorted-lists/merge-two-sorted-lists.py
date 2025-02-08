# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        res = ListNode(0)
        cur = res
        while h1 and h2:
            cur.next = ListNode(min(h1.val, h2.val))
            cur = cur.next
            if h1.val < h2.val:
                h1 = h1.next
            else:
                h2 = h2.next
        
        if h1:
            cur.next = h1
        elif h2:
            cur.next = h2
        
        return res.next