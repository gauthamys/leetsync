class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "1":
                    continue
                q = [(i, j)]
                while q:
                    curI, curJ = q.pop()
                    grid[curI][curJ] = "0"
                    children = [
                        (curI + 1, curJ), 
                        (curI - 1, curJ), 
                        (curI, curJ + 1), 
                        (curI, curJ - 1)
                    ]
                    for x, y in children:
                        if x < 0 or x > rows - 1 or y < 0 or y > cols - 1:
                            continue
                        if grid[x][y] == "1": 
                            q.append((x, y))
                res += 1
        return res