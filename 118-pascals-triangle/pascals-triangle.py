class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for _ in range(numRows - 1):
            top = triangle[-1]
            nex = []
            for i in range(1, len(top)):
                nex.append(top[i] + top[i - 1])
            nex = [1] + nex + [1]
            triangle.append(nex)
        return triangle