class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}

        for src, dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        
        q = []
        for node in adj:
            if indegree[node] == 0:
                q.append(node)

        finished = 0
        while q:
            cur = q.pop(0)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            finished += 1
        
        return finished == numCourses