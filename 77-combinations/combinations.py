class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(cur, num):
            nonlocal res
            if len(cur) == k:
                res.append(cur)
                return
            for i in range(num + 1, n + 1):
                dfs(cur + [i], i)
        dfs([], 0)
        return res
                