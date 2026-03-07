class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {(len(s), 0): True}
        def backtrack(start, openCount):
            if openCount < 0:
                dp[(start, openCount)] = False
                return False

            if (start, openCount) in dp:
                return dp[(start, openCount)]

            if start == len(s):
                dp[(start, openCount)] = False
                return False
            
            if s[start] == '(':
                dp[(start, openCount)] = backtrack(start + 1, openCount + 1)
            
            elif s[start] == ')':
                dp[(start, openCount)] = backtrack(start + 1, openCount - 1)
            
            else:
                dp[(start, openCount)] = backtrack(start + 1, openCount + 1) or backtrack(start + 1, openCount - 1) or backtrack(start + 1, openCount)
            
            return dp[(start, openCount)]

        return backtrack(0, 0)

            
            