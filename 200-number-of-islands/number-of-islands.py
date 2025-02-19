class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    islands += 1
                    stk = [(i, j)]
                    while stk:
                        cur = stk.pop()
                        for d in dirs:
                            r, c = cur[0] + d[0], cur[1] + d[1]
                            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or grid[r][c] != "1":
                                continue
                            grid[r][c] = "0"
                            stk.append((r, c))
        return islands  
