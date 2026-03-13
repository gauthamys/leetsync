class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        row = points[0]
        for r in range(1, ROWS):
            next_row = points[r].copy()
            left, right = [0] * COLS, [0] * COLS

            left[0] = row[0]
            for j in range(1, COLS):
                left[j] = max(row[j], left[j - 1] - 1)
            
            right[COLS - 1] = row[-1]
            for j in range(COLS - 2, -1, -1):
                right[j] = max(row[j], right[j + 1] - 1)
            
            for j in range(COLS):
                next_row[j] += max(left[j], right[j])

            row = next_row
        
        return max(row)