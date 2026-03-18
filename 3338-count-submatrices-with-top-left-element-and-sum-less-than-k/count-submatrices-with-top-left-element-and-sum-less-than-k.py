class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        res = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                if dp[i][j] <= k:
                    res += 1
        
        return res
