class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != 'O' or (i, j) in visited:
                    continue
                
                visited.add((i, j))
                q = deque([(i, j)])
                path = []
                surrounded = True

                while q:
                    cur_i, cur_j = q.popleft()
                    if cur_i in [0, rows - 1] or cur_j in [0, cols - 1]:
                        surrounded = False
                    
                    path.append((cur_i, cur_j))
                    children = [
                        (cur_i + 1, cur_j),
                        (cur_i - 1, cur_j),
                        (cur_i, cur_j + 1),
                        (cur_i, cur_j - 1)
                    ]
                    
                    for ci, cj in children:
                        if ci < 0 or ci >= rows or cj < 0 or cj >= cols or (ci, cj) in visited or board[ci][cj] != 'O':
                            continue
                        
                        visited.add((ci, cj))
                        q.append((ci, cj))
                
                if surrounded:
                    for x_i, x_j in path:
                        board[x_i][x_j] = 'X'
