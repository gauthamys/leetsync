class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list) # (x, y): [(weight, x, y))]
        for x, y in points:
            for x_2, y_2 in points:
                distance = abs(x - x_2) + abs(y - y_2)
                adj[(x, y)].append((distance, (x_2, y_2)))
        
        minHeap = [(0, points[0][0], points[0][1])]
        visited = set()
        res = 0

        while minHeap:
            distance, x, y = heapq.heappop(minHeap)
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            res += distance

            for w, nei in adj[(x, y)]:
                x_2, y_2 = nei
                if (x_2, y_2) in visited:
                    continue

                newDistance = abs(x - x_2) + abs(y - y_2)
                heapq.heappush(minHeap, (newDistance, x_2, y_2))
        
        return res