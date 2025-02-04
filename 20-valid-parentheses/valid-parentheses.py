class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stk.append(i)
            else:
                if len(stk) == 0: return False
                elif (i == '}' and stk[-1] == '{') or (i == ')' and stk[-1] == '(') or (i == ']' and stk[-1] == '['):
                    stk.pop()
                else: return False
        return len(stk) == 0