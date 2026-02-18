class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            i, j = 0, 0
            while i < len(res) and j < len(s) and res[i] == s[j]:
                i += 1
                j += 1
            res = res[:i]
        return res