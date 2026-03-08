class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        towers = [[0] * 101 for _ in range(101)]
        towers[0][0] = poured
        for row in range(query_row + 1):
            for j in range(row + 1):
                if towers[row][j] < 1:
                    continue
                excess = towers[row][j] - 1
                towers[row][j] = 1
                towers[row + 1][j] += excess / 2
                towers[row + 1][j + 1] += excess / 2
        
        return towers[query_row][query_glass]