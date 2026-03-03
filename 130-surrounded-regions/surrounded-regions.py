class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])
        q = deque([])

        def check(i, j):
            return i < rows and i >= 0 and j < cols and j >= 0 and board[i][j] == 'O' and (i, j) not in visited
        
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
                if check(cur_i + 1, cur_j):
                    q.append((cur_i + 1, cur_j))
                    visited.add((cur_i + 1, cur_j))
                
                if check(cur_i - 1, cur_j):
                    q.append((cur_i - 1, cur_j))
                    visited.add((cur_i - 1, cur_j))
                
                if check(cur_i, cur_j + 1):
                    q.append((cur_i, cur_j + 1))
                    visited.add((cur_i, cur_j + 1))
                
                if check(cur_i, cur_j - 1):
                    q.append((cur_i, cur_j - 1))
                    visited.add((cur_i, cur_j - 1))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'


        