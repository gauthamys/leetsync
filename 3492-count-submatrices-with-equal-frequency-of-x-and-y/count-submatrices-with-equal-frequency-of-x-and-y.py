class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[(0, 0)] * (cols + 1) for _ in range(rows + 1)]
        res = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                left_x, left_y = dp[i][j - 1]
                top_x, top_y = dp[i - 1][j]
                diag_x, diag_y = dp[i - 1][j - 1]
                
                x_count = left_x + top_x - diag_x
                y_count = left_y + top_y - diag_y
                if grid[i - 1][j - 1] == 'X':
                    x_count += 1
                elif grid[i - 1][j - 1] == 'Y':
                    y_count += 1
                
                if x_count == y_count and x_count > 0:
                    res += 1
                
                dp[i][j] = (x_count, y_count)
        
        return res
