class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        q = [(i, j, 0) for i in range(ROWS) for j in range(COLS) if rooms[i][j] == 0]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur = q.pop(0)
                visited.add((cur[0], cur[1]))
                for d in dirs:
                    r, c = cur[0] + d[0], cur[1] + d[1]
                    cost = cur[2]
                    if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or rooms[r][c] == -1 or rooms[r][c] == 0 or (r, c) in visited:
                        continue

                    rooms[r][c] = min(rooms[r][c], cost + 1)
                    visited.add((r, c))
                    q.append((r, c, rooms[r][c]))