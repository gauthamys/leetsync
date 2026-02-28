class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        
        q = deque([])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] != 0:
                    continue
                q.append((i, j, 0))
                visited.add((i, j))
        
        while q:
            cur_i, cur_j, path_len = q.popleft()
            children = [
                (cur_i + 1, cur_j), 
                (cur_i - 1, cur_j), 
                (cur_i, cur_j + 1), 
                (cur_i, cur_j - 1)
            ]
            for ci, cj in children:
                if ci < 0 or cj < 0 or ci >= rows or cj >= cols or rooms[ci][cj] == -1 or (ci, cj) in visited:
                    continue
                visited.add((ci, cj))
                q.append((ci, cj, path_len + 1))
                rooms[ci][cj] = min(rooms[ci][cj], path_len + 1)
            
                