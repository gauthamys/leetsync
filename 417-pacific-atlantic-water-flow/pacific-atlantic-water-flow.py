class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        q = deque()
        # left and top for pacific
        for i in range(rows):
            q.append((i, 0))
        for j in range(cols):
            q.append((0, j))
        
        pac = set(q)
        while q:
            cur_i, cur_j = q.popleft()
            children = [
                (cur_i + 1, cur_j),
                (cur_i - 1, cur_j),
                (cur_i, cur_j + 1),
                (cur_i, cur_j - 1)
            ]
            for ci, cj in children:
                if ci < 0 or cj < 0 or ci >= rows or cj >= cols or (ci, cj) in pac:
                    continue
                if heights[ci][cj] >= heights[cur_i][cur_j]:
                    pac.add((ci, cj))
                    q.append((ci, cj))

        q = deque()
        # right and bottom for atlantic
        for i in range(rows):
            q.append((i, cols - 1))
        for j in range(cols):
            q.append((rows - 1, j))

        atl = set(q)
        while q:
            cur_i, cur_j = q.popleft()
            children = [
                (cur_i + 1, cur_j),
                (cur_i - 1, cur_j),
                (cur_i, cur_j + 1),
                (cur_i, cur_j - 1)
            ]
            for ci, cj in children:
                if ci < 0 or cj < 0 or ci >= rows or cj >= cols or (ci, cj) in atl:
                    continue
                if heights[ci][cj] >= heights[cur_i][cur_j]:
                    atl.add((ci, cj))
                    q.append((ci, cj))
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i, j])
        return res
        

