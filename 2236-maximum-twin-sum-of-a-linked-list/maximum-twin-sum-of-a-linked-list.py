# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        a = []
        n = 0
        res = 0

        while cur:
            a.append(cur.val)
            cur = cur.next
            n += 1
        
        l, r = 0, n - 1
        while l < r:
            res = max(res, a[l] + a[r])
            l += 1
            r -= 1
        return res

        
