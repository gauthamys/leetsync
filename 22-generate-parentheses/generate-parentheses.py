class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def backtrack(openCount, closeCount):
            if openCount == n and closeCount == n and len(cur[:]) == 2 * n:
                res.append(''.join(cur[:]))
                return
            
            if openCount < n:
                cur.append('(')
                backtrack(openCount + 1, closeCount)
                cur.pop()
            
            if openCount > closeCount:
                cur.append(')')
                backtrack(openCount, closeCount + 1)
                cur.pop()
        
        backtrack(0, 0)
        return res