class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            cur = 0
            for j in range(n):
                cur += matrix[i][j]
                self.prefix[i][j] = cur

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                res += self.prefix[i][col2]
            else: 
                res += self.prefix[i][col2] - self.prefix[i][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)