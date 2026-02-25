class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(st):
            return st == st[::-1]
        
        res = []
        cur = []
        def backtrack(start):
            if start >= len(s):
                res.append(cur[:])
                return
            for end in range(start + 1, len(s) + 1):
                piece = s[start:end]
                if isPalindrome(piece):
                    cur.append(piece)
                    backtrack(end)
                    cur.pop()
        
        backtrack(0)
        return res
