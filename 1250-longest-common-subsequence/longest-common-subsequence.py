class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i - 1, j - 1)
            else:
                return max(dfs(i - 1, j), dfs(i, j - 1))  
        
        return max(dfs(i, j) for i in range(len(text1)) for j in range(len(text2)))          
