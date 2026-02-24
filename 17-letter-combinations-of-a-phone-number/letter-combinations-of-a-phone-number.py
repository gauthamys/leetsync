class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
        res = []
        def dfs(index, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            possible = m[digits[index]]
            for letter in possible:
                dfs(index + 1, cur + letter)
        dfs(0, "")
        return res
