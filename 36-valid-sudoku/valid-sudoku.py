class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rset = defaultdict(set)
        cset = defaultdict(set)
        subset = defaultdict(set)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                subIndex = 3 * (i // 3) + (j // 3)
                if (board[i][j] in rset[i]) or (board[i][j] in cset[j]) or (board[i][j] in subset[subIndex]):
                    return False

                rset[i].add(board[i][j])
                cset[j].add(board[i][j])
                subset[subIndex].add(board[i][j])

        return True
