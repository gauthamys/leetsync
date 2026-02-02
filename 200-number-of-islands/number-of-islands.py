class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0":
                    continue
                stk = [(i, j)]
                while stk:
                    curI, curJ = stk.pop()
                    for dI, dJ in dirs:
                        if curI + dI < ROWS and curI + dI >= 0 and curJ + dJ >= 0 and curJ + dJ < COLS and grid[curI + dI][curJ + dJ] == "1":
                            stk.append((curI + dI, curJ + dJ))
                            grid[curI + dI][curJ + dJ] = "0"
                res += 1
        return res