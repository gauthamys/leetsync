from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        degree = [0] * n
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degree[b] += 1
            degree[a] += 1
        
        q = deque([node for node in adj if degree[node] == 1])
        while q:
            if n <= 2:
                return list(q)
            for _ in range(len(q)):
                cur = q.popleft()
                n -= 1
                for nei in adj[cur]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        q.append(nei)
        
        return [node for node in adj if node not in q]