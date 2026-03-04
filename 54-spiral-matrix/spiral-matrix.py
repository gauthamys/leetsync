class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        ROWS, COLS = b, r
        res = []
        L, R, U, D = 'L', 'R', 'U', 'D'
        d = R
        i, j = 0, 0
        while t < b and l < r:
            res.append(matrix[i][j])
            if d == R: 
                if j == r - 1:
                    t += 1
                    d = D
                    i += 1
                    continue
                j += 1
            
            if d == D: 
                if i == b - 1:
                    r -= 1
                    d = L
                    j -= 1
                    continue
                i += 1
            
            if d == L:
                if j == l:
                    b -= 1
                    d = U
                    i -= 1
                    continue
                j -= 1
            
            if d == U:
                if i == t:
                    l += 1
                    d = R
                    j += 1
                    continue
                i -= 1

        return res
