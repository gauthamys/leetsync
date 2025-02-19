class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        q = [i for i in range(len(indegree)) if indegree[i] == 0]

        finished = 0
        while q:
            cur = q.pop(0)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            finished += 1
        
        return finished == numCourses
        
        