class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for tok in tokens:
            if tok in ['+', '-', '/', '*']:
                op2 = int(stk.pop())
                op1 = int(stk.pop())
                if tok == '+':
                    stk.append(str(op1 + op2))
                elif tok == '-':
                    stk.append(str(op1 - op2))
                elif tok == '*':
                    stk.append(str(op1 * op2))
                else:
                    stk.append(str(int(op1 / op2)))
            else:
                stk.append(tok)
        return int(stk[0])