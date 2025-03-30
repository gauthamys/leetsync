class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        q = [(entrance, 0)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur = q.pop(0)
                pos, steps = cur[0], cur[1]
                for d in dirs:
                    r = pos[0] + d[0]
                    c = pos[1] + d[1]
                    if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1:
                        if pos != entrance:
                            return steps
                    elif maze[r][c] == ".":
                        maze[r][c] = "+"
                        q.append(([r, c], steps + 1))
        return -1

