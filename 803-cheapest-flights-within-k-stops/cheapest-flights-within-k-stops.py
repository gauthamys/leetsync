import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # steps = number of edges used so far
        # allow up to k+1 edges (because k stops = k intermediate nodes)
        max_steps = k + 1

        # best[city][steps] = min cost to reach city using exactly steps edges (or min so far)
        best = [[float('inf')] * (max_steps + 1) for _ in range(n)]
        best[src][0] = 0

        heap = [(0, src, 0)]  # cost, city, steps

        while heap:
            cost, u, steps = heapq.heappop(heap)

            if u == dst:
                return cost

            if cost > best[u][steps]:
                continue

            if steps == max_steps:
                continue

            for v, w in adj[u]:
                nc = cost + w
                ns = steps + 1
                if nc < best[v][ns]:
                    best[v][ns] = nc
                    heapq.heappush(heap, (nc, v, ns))

        return -1