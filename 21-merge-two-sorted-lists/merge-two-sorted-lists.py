# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        res = ListNode()
        cur = res
        while cur1 and cur2:
            if cur1.val < cur2.val:
                new = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                new = ListNode(cur2.val)
                cur2 = cur2.next
            cur.next = new
            cur = cur.next
        
        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2
        
        return res.next