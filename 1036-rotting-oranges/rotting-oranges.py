class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        minutes = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                curI, curJ = q.pop(0)
                if curI + 1 < ROWS and grid[curI + 1][curJ] == 1:
                    grid[curI + 1][curJ] = 2
                    q.append((curI + 1, curJ))
                if curI - 1 >= 0 and grid[curI - 1][curJ] == 1:
                    grid[curI - 1][curJ] = 2
                    q.append((curI - 1, curJ))
                if curJ + 1 < COLS and grid[curI][curJ + 1] == 1:
                    grid[curI][curJ + 1] = 2
                    q.append((curI, curJ + 1))
                if curJ - 1 >= 0 and grid[curI][curJ - 1] == 1:
                    grid[curI][curJ - 1] = 2
                    q.append((curI, curJ - 1))
            if q:
                minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes