class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk = []
        res = ""
        temp = ""
        for c in s:
            if c == "(":
                stk.append(c)
                if len(stk) > 1:
                    temp += c
            else:
                stk.pop()
                if len(stk) == 0:
                    res += temp
                    temp = ''
                else:
                    temp += c
        return res

# ( ()() )( () )
# stk _
# stk (, temp _
# stk ((, temp (
# stk (, temp ()
# stk ((, temp ()