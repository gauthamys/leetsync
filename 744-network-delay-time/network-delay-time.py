class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        minHeap = [(0, k)] # time, node
        visited = set()
        res = 0
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)

            if len(visited) == n:
                res = max(res, t)
            
            for nei, w in adj[node]:
                if nei in visited:
                    continue
                newTime = t + w
                heapq.heappush(minHeap, (newTime, nei))

        return res if len(visited) == n else -1
        