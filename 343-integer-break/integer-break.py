class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        
        for i in range(4):
            dp[i] = i

        for i in range(4, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * dp[i - j])
        
        return dp[n]