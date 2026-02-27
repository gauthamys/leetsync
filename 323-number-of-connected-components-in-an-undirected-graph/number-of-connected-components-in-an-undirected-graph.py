class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # nodes: 0, 1, ... , n - 1
        
        visited = set()
        res = 0
        for start in range(n):
            if start in visited:
                continue
            
            q = [start]
            while q:
                cur = q.pop(0)
                visited.add(cur)
                for nei in adj[cur]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
            
            res += 1
        
        return res