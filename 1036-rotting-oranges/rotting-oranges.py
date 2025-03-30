class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        minutes = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur = q.pop(0)
                for d in dirs:
                    r = cur[0] + d[0]
                    c = cur[1] + d[1]
                    if r > ROWS - 1 or r < 0 or c > COLS - 1 or c < 0 or grid[r][c] != 1:
                        continue
                    q.append((r, c))
                    grid[r][c] = 2
            if q:
                minutes += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        
        return minutes