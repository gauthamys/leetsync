class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        d = 'DOWN'
        cur = 0
        for c in s:
            rows[cur].append(c)
            if d == 'DOWN':
                if cur < numRows - 1:
                    cur += 1
                else:
                    d = 'UP'
                    cur -= 1
            else:
                if cur > 0:
                    cur -= 1
                else:
                    d = "DOWN"
                    cur += 1
        return ''.join(''.join(x) for x in rows)
                
            