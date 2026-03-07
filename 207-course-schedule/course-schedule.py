class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        degree = [0] * numCourses

        for u, v in prerequisites:
            adj[u].append(v)
            degree[v] += 1
        
        q = deque([crs for crs in range(numCourses) if degree[crs] == 0])
        finished = set()

        while q:
            cur = q.popleft()
            finished.add(cur)
            for nei in adj[cur]:
                if nei in finished:
                    continue
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)
        
        return len(finished) == numCourses