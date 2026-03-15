class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i == 0:
                return grid[i][j]  + dfs(i, j - 1)
            if j == 0:
                return grid[i][j] + dfs(i - 1, j)
            
            return grid[i][j] + min(dfs(i - 1, j), dfs(i, j - 1))
        
        rows, cols = len(grid), len(grid[0])
        return dfs(rows - 1, cols - 1)
            
