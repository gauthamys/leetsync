class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i , j) not in visited:
                    islands += 1
                    q = [(i, j)]
                    visited.add((i, j))
                    while q:
                        cur = q.pop(0)
                        for d in dirs:
                            r, c = cur[0] + d[0], cur[1] + d[1]
                            if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or grid[r][c] != "1" or (r, c) in visited:
                                continue
                            q.append((r, c))
                            visited.add((r, c))
        return islands