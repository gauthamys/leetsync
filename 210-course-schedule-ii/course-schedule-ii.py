class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        q = [crs for crs in range(numCourses) if indegree[crs] == 0]
        res = []
        while q:
            cur = q.pop(0)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(cur)
        
        return res[::-1] if len(res) == numCourses else []
                