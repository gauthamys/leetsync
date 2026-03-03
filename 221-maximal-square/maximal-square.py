class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        res = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] != '1':
                    continue
                
                left = dp[i][j - 1]
                top = dp[i - 1][j]
                diag = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(left, top, diag)
                res = max(res, dp[i][j])
        
        return res * res