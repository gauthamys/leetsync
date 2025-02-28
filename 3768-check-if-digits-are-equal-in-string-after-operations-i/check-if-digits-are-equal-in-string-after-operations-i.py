class Solution:
    def hasSameDigits(self, s: str) -> bool:
        new = s
        while len(new) > 2:
            tmp = ""
            for i in range(1, len(new)):
                a, b = int(new[i - 1]), int(new[i])
                tmp += str((a + b) % 10)
            new = tmp
        
        return new[0] == new[1]
        
        

