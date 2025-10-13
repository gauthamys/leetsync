class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        def bfs(r, c):
            visited = set()
            visited.add((r, c))
            queue = [(r, c)]
            atl = False
            pac = False
            while queue:
                cr, cc = queue.pop(0)
                if cr == ROWS - 1 or cc == COLS - 1:
                    atl = True
                if cr == 0 or cc == 0:
                    pac = True
                if pac == True and atl == True:
                    return True

                if cr + 1 < ROWS and heights[cr + 1][cc] <= heights[cr][cc] and (cr + 1, cc) not in visited:
                    queue.append((cr + 1, cc))
                    visited.add((cr + 1, cc))
                if cr - 1 >= 0 and heights[cr - 1][cc] <= heights[cr][cc] and (cr - 1, cc) not in visited:
                    queue.append((cr - 1, cc))
                    visited.add((cr - 1, cc))
                if cc + 1 < COLS and heights[cr][cc + 1] <= heights[cr][cc] and (cr, cc + 1) not in visited:
                    queue.append((cr, cc + 1))
                    visited.add((cr, cc + 1))
                if cc - 1 >= 0 and heights[cr][cc - 1] <= heights[cr][cc] and (cr, cc - 1) not in visited:
                    queue.append((cr, cc - 1))
                    visited.add((cr, cc - 1))
            
            return pac and atl
        
        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i, j):
                    res.append((i, j))
        
        return res