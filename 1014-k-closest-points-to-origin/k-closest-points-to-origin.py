class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(maxHeap, (-dist, x, y))
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [(x, y) for _, x, y in maxHeap]
