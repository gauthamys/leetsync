class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        minHeap = [(0, 0)] # (cost, point_index)
        edges_used = 0
        res = 0

        while edges_used < n:
            cost, u = heapq.heappop(minHeap)
            if visited[u]:
                continue
            
            visited[u] = True
            edges_used += 1
            res += cost

            for v in range(n):
                if visited[v]:
                    continue
                distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(minHeap, (distance, v))
        
        return res