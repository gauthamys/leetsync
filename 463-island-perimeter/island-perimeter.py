class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                res += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    res -= 2
                if j + 1 < COLS and grid[i][j + 1] == 1:
                    res -= 2
        return res