class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(start, pathLen):
            if pathLen == k:
                res.append(cur[:])
                return
            if start > n:
                return
            for i in range(start, n + 1):
                cur.append(i)
                backtrack(i + 1, pathLen + 1)
                cur.pop()
        backtrack(1, 0)
        return res