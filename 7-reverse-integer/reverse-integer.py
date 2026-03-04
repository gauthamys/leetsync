class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = x // abs(x)
        res = sign * int(str(abs(x))[::-1])
        
        if res >= (2 ** 31) - 1 or res <= -1 * (2 ** 31):
            return 0
        
        return res