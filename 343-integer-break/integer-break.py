class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)
        
        for i in range(4):
            dp[i] = i

        for i in range(4, n + 1):
            ans = i
            for j in range(2, i):
                ans = max(ans, j * dp[i - j])
            dp[i] = ans
        
        return dp[n]