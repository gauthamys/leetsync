class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    print(i, j)
                    q = []
                    visited.add((i, j))
                    q.append((i, j))

                    while len(q) > 0:
                        cur = q.pop(0)
                        curI, curJ = cur[0], cur[1]
                        if curI + 1 < ROWS and grid[curI + 1][curJ] == '1' and (curI + 1, curJ) not in visited:
                            q.append((curI + 1, curJ))
                            visited.add((curI + 1, curJ))
                        if curI - 1 >= 0 and grid[curI - 1][curJ] == '1' and (curI - 1, curJ) not in visited:
                            q.append((curI - 1, curJ))
                            visited.add((curI - 1, curJ))
                        if curJ + 1 < COLS and grid[curI][curJ + 1] == '1' and (curI, curJ + 1) not in visited:
                            q.append((curI, curJ + 1))
                            visited.add((curI, curJ + 1))
                        if curJ - 1 >= 0 and grid[curI][curJ - 1] == '1' and (curI, curJ - 1) not in visited:
                            q.append((curI, curJ - 1))
                            visited.add((curI, curJ - 1))
                    
                    res += 1
        
        return res