class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])
        q = deque([])
        
        # left and right
        for i in range(rows):
            if board[i][0] == 'O':
                q.append((i, 0))
                visited.add((i, 0))
            
            if board[i][cols - 1] == 'O':
                q.append((i, cols - 1))
                visited.add((i, cols - 1))
        
        # top and bottom
        for j in range(cols):
            if board[0][j] == 'O':
                q.append((0, j))
                visited.add((0, j))
            
            if board[rows - 1][j] == 'O':
                q.append((rows - 1, j))
                visited.add((rows - 1, j))
        
        while q:
            qLen = len(q)
            for _ in range(qLen):
                cur_i, cur_j = q.popleft()
                if cur_i + 1 < rows and board[cur_i + 1][cur_j] == 'O' and (cur_i + 1, cur_j) not in visited:
                    q.append((cur_i + 1, cur_j))
                    visited.add((cur_i + 1, cur_j))
                
                if cur_i - 1 >= 0 and board[cur_i - 1][cur_j] == 'O' and (cur_i - 1, cur_j) not in visited:
                    q.append((cur_i - 1, cur_j))
                    visited.add((cur_i - 1, cur_j))
                
                if cur_j + 1 < cols and board[cur_i][cur_j + 1] == 'O' and (cur_i, cur_j + 1) not in visited:
                    q.append((cur_i, cur_j + 1))
                    visited.add((cur_i, cur_j + 1))
                
                if cur_j - 1 >= 0 and board[cur_i][cur_j - 1] == 'O' and (cur_i, cur_j - 1) not in visited:
                    q.append((cur_i, cur_j - 1))
                    visited.add((cur_i, cur_j - 1))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'


        