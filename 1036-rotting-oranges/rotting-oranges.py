class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                start = q.pop(0)
                for d in dirs:
                    r = start[0] + d[0] 
                    c = start[1] + d[1]
                    if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append((r, c))
            if q:
                minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes