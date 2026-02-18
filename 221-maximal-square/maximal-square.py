class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        left = dp[i][j - 1]
                        up = dp[i - 1][j]
                        diag = dp[i - 1][j - 1]
                        dp[i][j] = min(left, up, diag) + 1
                res = max(res, dp[i][j])
        
        return res * res
