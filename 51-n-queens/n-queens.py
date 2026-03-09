class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set()
        anti = set()
        res = []
        cur = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in cur])
                return
            
            for c in range(n):
                if c in cols or (r + c) in anti or (r - c) in diag:
                    continue
                cols.add(c)
                diag.add((r - c))
                anti.add((r + c))

                cur[r][c] = 'Q'
                backtrack(r + 1)
                cur[r][c] = '.'

                cols.remove(c)
                diag.remove((r - c))
                anti.remove((r + c))
        
        backtrack(0)
        return res
                