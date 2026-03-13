class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if s[l] == s[r]:
                return dfs(l + 1, r - 1) + 2
            else:
                return max(dfs(l + 1, r), dfs(l, r - 1))
        
        return dfs(0, n - 1)