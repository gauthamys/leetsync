class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        r_mid, c_mid = -1, -1
        while t <= b:
            r_mid = (t + b) // 2
            if matrix[r_mid][l] <= target and matrix[r_mid][r] >= target:
                break
            if matrix[r_mid][l] > target:
                b = r_mid - 1
            else:
                t = r_mid + 1
        
        if t > b:
            return False
        
        while l <= r:
            c_mid = (l + r) // 2
            if matrix[r_mid][c_mid] == target:
                return True
            if matrix[r_mid][c_mid] > target:
                r = c_mid - 1
            else:
                l = c_mid + 1
        
        return False
