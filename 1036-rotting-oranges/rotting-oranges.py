class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0
        q = []
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            qLen = len(q)
            for _ in range(qLen):
                curI, curJ = q.pop(0)
                for dI, dJ in dirs:
                    newI = curI + dI
                    newJ = curJ + dJ
                    if newI < ROWS and newI >= 0 and newJ < COLS and newJ>= 0 and grid[newI][newJ] == 1 and (newI, newJ) not in visited:
                        q.append((newI, newJ))
                        visited.add((newI, newJ))
            if q:
                minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        
        return minutes