class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ']':
                cur = ''
                while stk[-1] != '[':
                    cur += stk.pop()
                stk.pop() # remove '['
                mult = ''
                while stk and stk[-1] in '0123456789':
                    mult += stk.pop()
                mult = int(mult[::-1])
                #mult = int(stk.pop()) # get K
                for ch in (cur * mult)[::-1]:
                    stk.append(ch)
            else:
                stk.append(c)
        return ''.join(stk)
        