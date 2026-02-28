class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        q = deque([(0, -1)])
        visited.add(0)
        while q: # Checking Connected
            cur, parent = q.popleft()
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                q.append((nei, cur))
                visited.add(nei)
        
        return len(visited) == n
            