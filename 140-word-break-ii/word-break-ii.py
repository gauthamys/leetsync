class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        cur = []
        def backtrack(start):
            if start == len(s):
                res.append(' '.join(cur))
                return

            for word in wordDict:
                if start + len(word) <= len(s) and s[start:start + len(word)] == word:
                    cur.append(word)
                    backtrack(start + len(word))
                    cur.pop()

        backtrack(0)
        return res
                    