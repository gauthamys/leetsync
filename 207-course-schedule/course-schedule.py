class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        visited = set()
        def dfs(cnum):
            if adj[cnum] == []:
                return True
            if cnum in visited:
                return False
            visited.add(cnum)
            for p in adj[cnum]:
                if not dfs(p): 
                    return False

            visited.remove(cnum)
            adj[cnum] = []
            return True

        for course in adj.keys():
            if not dfs(course):
                return False
        
        return True
