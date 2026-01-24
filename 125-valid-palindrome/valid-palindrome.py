class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_char(x):
            return (ord(x) >= ord('a') and ord(x) <= ord('z')) or (ord(x) >= ord('0') and ord(x) <= ord('9'))
        
        l, r = 0, len(s) - 1
        s = s.lower()
        print(s)
        while l < r:
            while not is_char(s[l]) and l < r:
                l += 1
            while not is_char(s[r]) and l < r:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True