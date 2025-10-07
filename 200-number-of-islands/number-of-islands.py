class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j):
                    q = [(i, j)]
                    while q:
                        curI, curJ = q.pop(0)
                        grid[curI][curJ] = "0"
                        if curI + 1 < ROWS and grid[curI + 1][curJ] == "1" and (curI + 1, curJ):
                            q.append((curI + 1, curJ))
                            grid[curI + 1][curJ] = "0"
                        if curI - 1 >= 0 and grid[curI - 1][curJ] == "1" and (curI - 1, curJ):
                            q.append((curI - 1, curJ))
                            grid[curI - 1][curJ] = "0"
                        if curJ + 1 < COLS and grid[curI][curJ + 1] == "1" and (curI, curJ + 1):
                            q.append((curI, curJ + 1))
                            grid[curI][curJ + 1] = "0"
                        if curJ - 1 >= 0 and grid[curI][curJ - 1] == "1" and (curI, curJ - 1):
                            q.append((curI, curJ - 1))
                            grid[curI][curJ - 1] = "0"
                    islands += 1
        
        return islands