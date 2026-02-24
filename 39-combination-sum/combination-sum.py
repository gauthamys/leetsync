class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(cur):
            if sum(cur) == target:
                if tuple(sorted(cur)) not in visited:
                    res.append(cur)
                    visited.add(tuple(sorted(cur)))
                return
            if sum(cur) > target:
                return
            else:
                for j in range(len(candidates)):
                    dfs(cur + [candidates[j]])
        dfs([])
        return res
            