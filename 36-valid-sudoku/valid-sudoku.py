class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        r = defaultdict(set)
        c = defaultdict(set)
        s = defaultdict(set)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == '.':
                    continue
                n = board[i][j]
                sub_key = 3*(i//3) + j//3
                if n in r[i] or n in c[j] or n in s[sub_key]:
                    return False
                r[i].add(n)
                c[j].add(n)
                s[sub_key].add(n)
        return True
