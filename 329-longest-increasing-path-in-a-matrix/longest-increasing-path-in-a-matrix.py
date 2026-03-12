class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        
        def dfs(i, j):
            if memo[i][j] > 0:
                return memo[i][j]

            best = 1
            for nr, nc in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[i][j]:
                    best = max(best, 1 + dfs(nr, nc))
            
            memo[i][j] = best
            return best
        
        return max(dfs(i, j) for i in range(rows) for j in range(cols))
