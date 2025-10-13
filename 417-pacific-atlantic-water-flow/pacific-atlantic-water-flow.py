class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        atl = set()
        pac = set()
        def bfs(r, c, visited):
            visited.add((r, c))
            queue = [(r, c)]
            while queue:
                cr, cc = queue.pop(0)
                if cr + 1 < ROWS and heights[cr + 1][cc] >= heights[cr][cc] and (cr + 1, cc) not in visited:
                    queue.append((cr + 1, cc))
                    visited.add((cr + 1, cc))
                if cr - 1 >= 0 and heights[cr - 1][cc] >= heights[cr][cc] and (cr - 1, cc) not in visited:
                    queue.append((cr - 1, cc))
                    visited.add((cr - 1, cc))
                if cc + 1 < COLS and heights[cr][cc + 1] >= heights[cr][cc] and (cr, cc + 1) not in visited:
                    queue.append((cr, cc + 1))
                    visited.add((cr, cc + 1))
                if cc - 1 >= 0 and heights[cr][cc - 1] >= heights[cr][cc] and (cr, cc - 1) not in visited:
                    queue.append((cr, cc - 1))
                    visited.add((cr, cc - 1))
        
        for i in range(ROWS):
            bfs(i, 0, pac)
            bfs(i, COLS - 1, atl)
        for j in range(COLS):
            bfs(0, j, pac)
            bfs(ROWS - 1, j, atl)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in atl and (i, j) in pac:
                    res.append((i, j))
        
        return res