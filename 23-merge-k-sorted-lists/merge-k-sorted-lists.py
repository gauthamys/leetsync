# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        res = ListNode(-1)
        cur = res
        
        while any(lists[i] != None for i in range(len(lists))):
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                
                heapq.heappush(min_heap, lists[i].val)
                lists[i] = lists[i].next
            
            to_insert = heapq.heappop(min_heap)
            cur.next = ListNode(to_insert)
            cur = cur.next
        
        while min_heap:
            cur.next = ListNode(heapq.heappop(min_heap))
            cur = cur.next

        return res.next

