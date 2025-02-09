class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visited = set()
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        def dfs(cNum):
            if adj[cNum] == []:
                return True

            if cNum in visited:
                return False

            visited.add(cNum)
            for p in adj[cNum]:
                if not dfs(p):
                    return False
                    
            visited.remove(cNum)
            adj[cNum] = []
            return True

        for course in adj:
            if not dfs(course):
                return False
        
        return True
