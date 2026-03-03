class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)

        isReachable = [[False] * numCourses for _ in range(numCourses)]
        for i in range(numCourses):
            isReachable[i][i] = True

        for start in range(numCourses):
            q = deque([start])
            visited = set()
            visited.add(start)
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)
                    isReachable[start][nei] = True
        
        return [isReachable[i][j] for i, j in queries]