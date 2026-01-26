class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in ['[', '(', '{']:
                stk.append(c)
            else:
                if not stk:
                    return False
                top = stk[-1]
                if c == ')' and top != '(':
                    return False
                if c == ']' and top != '[':
                    return False
                if c == '}' and top != '{':
                    return False
                stk.pop(-1)
        return stk == []
                