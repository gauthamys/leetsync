class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(10)}
        cols = {i: set() for i in range(10)}
        sub = {i: set() for i in range(10)}

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                subIndex = (3 * (j // 3)) + (i // 3)
                print(subIndex)
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sub[subIndex]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sub[subIndex].add(board[i][j])
        return True
                
