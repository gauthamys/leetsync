from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        degree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            degree[a] += 1
        
        q = deque([node for node in adj if degree[node] == 0])
        finished = 0
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)
            finished += 1
        
        return finished == numCourses
