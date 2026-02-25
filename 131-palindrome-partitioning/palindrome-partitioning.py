class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st):
            return st == st[::-1]
        
        res = []
        def backtrack(start, cur):
            if start >= len(s):
                res.append(cur[:])
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if isPalindrome(piece):
                    backtrack(end, cur + [piece])
        
        backtrack(0, [])
        return res
