class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        res = []
        while q:
            cur = q.pop(0)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
            finished += 1
            res.append(cur)
        
        return list(reversed(res)) if finished == numCourses else []
