class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        MAX = 2 ** 31 - 1
        ROWS, COLS = len(rooms), len(rooms[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = []
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i, j))
        
        while q:
            cur = q.pop(0)
            for d in dirs:
                r = cur[0] + d[0]
                c = cur[1] + d[1]
                if r < 0 or r >= ROWS or c < 0 or c >= COLS or rooms[r][c] != MAX:
                    continue
                q.append((r, c))
                rooms[r][c] = rooms[cur[0]][cur[1]] + 1