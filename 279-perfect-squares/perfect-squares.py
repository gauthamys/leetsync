class Solution:
    def numSquares(self, n: int) -> int:
        sqs = []
        i = 1
        while i * i <= n:
            sqs.append(i * i)
            i += 1
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for sq in sqs:
            for i in range(sq, n + 1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
        
        return dp[n]