class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "0" or (i, j) in visited:
                    continue
                q = [(i, j)]
                visited.add((i, j))
                while q:
                    curI, curJ = q.pop(0)
                    if curI + 1 < ROWS and grid[curI + 1][curJ] == "1" and (curI + 1, curJ) not in visited:
                        q.append((curI + 1, curJ))
                        visited.add((curI + 1, curJ))
                    if curJ + 1 < COLS and grid[curI][curJ + 1] == "1" and (curI, curJ + 1) not in visited:
                        q.append((curI, curJ + 1))
                        visited.add((curI, curJ + 1))
                    if curI - 1 >= 0 and grid[curI - 1][curJ] == "1" and (curI - 1, curJ) not in visited:
                        q.append((curI - 1, curJ))
                        visited.add((curI - 1, curJ))
                    if curJ - 1 >= 0 and grid[curI][curJ - 1] == "1" and (curI, curJ - 1) not in visited:
                        q.append((curI, curJ - 1))
                        visited.add((curI, curJ - 1))
                res += 1
    
        return res