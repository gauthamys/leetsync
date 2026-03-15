class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {(0, 0): grid[0][0]}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == 0:
                return grid[i][j]  + dfs(i, j - 1)
            if j == 0:
                return grid[i][j] + dfs(i - 1, j)
            memo[(i, j)] = grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
            return memo[(i, j)]
        
        rows, cols = len(grid), len(grid[0])
        return dfs(rows - 1, cols - 1)
            
