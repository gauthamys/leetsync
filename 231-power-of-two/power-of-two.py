class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        cur = n
        while cur % 2 != 1:
            cur //= 2
        
        return cur == 1
        
