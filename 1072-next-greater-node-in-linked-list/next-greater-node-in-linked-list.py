# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        res = [0] * n
        stk = [] # (idx, node)
        cur = head
        i = 0

        while cur:
            while stk and stk[-1][1].val < cur.val:
                idx, _ = stk.pop()
                res[idx] = cur.val
            stk.append((i, cur))
            i += 1
            cur = cur.next
        
        return res
