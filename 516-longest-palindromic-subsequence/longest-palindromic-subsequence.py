class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)] # states: (i, j)
        
        # BASE CASES (odd palindromes)
        for i in range(len(s)):
            dp[i][i] = 1

        # BASE CASES (even palindromes)
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                dp[i - 1][i] = 2

        # Bottom Up while reusing states
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i > 1):
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][len(s) - 1]

                        
