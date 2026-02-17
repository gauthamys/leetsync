class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = "DOWN"
        arrs = [[] for _ in range(numRows)]
        i = 0
        for c in s:
            arrs[i].append(c)
            if d == "DOWN":
                if i < numRows - 1:
                    i += 1
                else:
                    d = "UP"
                    i -= 1
            elif d == "UP":
                if i > 0:
                    i -= 1
                else:
                    d = "DOWN"
                    i += 1
        return ''.join([''.join(arrs[i]) for i in range(numRows)])
                
                
                
