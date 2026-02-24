class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(i, cur):
            if sum(cur) == target:
                res.append(cur)
            if i >= len(candidates) or sum(cur) > target:
                return
            else:
                for j in range(i, len(candidates)):
                    dfs(j, cur + [candidates[j]])
        dfs(0, [])
        return res
            