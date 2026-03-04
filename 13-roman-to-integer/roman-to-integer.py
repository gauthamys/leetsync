class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] == 'I':
                res += 1
            
            if s[i] == 'V':
                res += 5
                if i > 0 and s[i - 1] == 'I':
                    res -= 2
            
            if s[i] == 'X':
                res += 10
                if i > 0 and s[i - 1] == 'I':
                    res -= 2
            
            if s[i] == 'L':
                res += 50
                if i > 0 and s[i - 1] == 'X':
                    res -= 20
            
            if s[i] == 'C':
                res += 100
                if i > 0 and s[i - 1] == 'X':
                    res -= 20
            
            if s[i] == 'D':
                res += 500
                if i > 0 and s[i - 1] == 'C':
                    res -= 200
            
            if s[i] == 'M':
                res += 1000
                if i > 0 and s[i - 1] == 'C':
                    res -= 200
        
        return res