class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = [-x for x in stones]
        heapq.heapify(l)
        
        while len(l) > 1:
            y = -heapq.heappop(l)
            x = -heapq.heappop(l)
            if x != y:
                heapq.heappush(l, x - y)

        return -l[0] if l else 0