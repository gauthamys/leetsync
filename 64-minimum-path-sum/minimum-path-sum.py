class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * (cols) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i - 1 < 0:
                    if j - 1 < 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j - 1 < 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])
        return dp[rows - 1][cols - 1]
