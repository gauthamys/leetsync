class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        def distance(p):
            return math.sqrt(p[0] ** 2 + p[1] ** 2)
        
        for point in points:
            heapq.heappush(h, (-distance(point), point))
            while len(h) > k:
                heapq.heappop(h)
        
        return [p[1] for p in h]