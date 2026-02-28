class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols = set()
        diag = set()
        anti = set()
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            
            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue
                
                cols.add(c)
                diag.add(r - c)
                anti.add(r + c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                cols.remove(c)
                diag.remove(r - c)
                anti.remove(r + c)
                board[r][c] = '.'
        
        backtrack(0)
        return res